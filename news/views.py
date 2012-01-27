# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2007, 2008, 2009, 2010 Peter Kuma
# All rights reserved.
#

import os

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils import translation
from django import forms
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from datetime import date

from tjrapid import settings
from tjrapid.main.models import *
from models import *

def archive(request,category,lang=settings.LANGUAGE_CODE,page=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	c = Category.objects.get(language__code=lang,name=category)
	a = Article.objects.filter(category=c)
	p = Paginator(a, 6)
	
	try:
		articles = p.page(page if page else 1)
	except (EmptyPage, InvalidPage):
		articles = p.page(1)
	
	return render_to_response(
		'news/archive/'+c.template_name, {
			'category': c,
			'articles': articles,
		},
		RequestContext(request)
	)

def details(request,category,lang=settings.LANGUAGE_CODE,id=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	try:
		c = Category.objects.get(language__code=lang,name=category)
		a = Article.objects.get(category=c,id=id)
	except ObjectDoesNotExist:
		raise Http404

	def comments_recur(objects,reply=None,level=0):
		out = []
		if reply != None:
			layer = objects.filter(reply=reply)
		else:
			layer = objects.filter(reply__isnull=True)
		for o in layer:
			out += [{'comment':o,'level':level}] + comments_recur(objects,o,level+1)
		return out
	
	comments = comments_recur(Comment.objects.filter(article=a))
	
	return render_to_response(
		'news/details/'+c.template_name, {
			'category': c,
			'article': a,
			'comments': comments,
		},
		RequestContext(request)
	)

def attachment(request,category,lang=settings.LANGUAGE_CODE,id=None,attachment=None):
	try:
		c = Category.objects.get(language__code=lang,name=category)
		article = Article.objects.get(category=c,id=id)
		for a in article.attachments.all():
			if os.path.basename(a.file.name) == attachment:
				return HttpResponseRedirect(a.file.url)
	except ObjectDoesNotExist:
		raise Http404
	raise Http404
	
def comment(request,category,lang=settings.LANGUAGE_CODE,id=None,reply_id=None):
	try:
		c = Category.objects.get(language__code=lang,name=category)
		a = Article.objects.get(category=c,id=id)
	except ObjectDoesNotExist:
		raise Http404
		
	try:
		reply = Comment.objects.get(id=reply_id)
		initial_subject = 'Re: %s' % reply.subject
	except ObjectDoesNotExist:
		reply = None
		initial_subject = None

	class CommentForm(forms.Form):
		subject = forms.CharField(label=_('Subject'),max_length=100,initial=initial_subject,
			widget=forms.TextInput(attrs={'size':'40'}))
		sender = forms.CharField(label=_('Sender'),max_length=50)
		message = forms.CharField(label=_('Message'),max_length=300,widget=forms.Textarea())
	
	comment = None
	if request.method == 'POST':
		f = CommentForm(request.POST)
		if f.is_valid():
			comment = Comment(
				article = a,
				reply = reply,
				subject = f.cleaned_data['subject'],
				message = f.cleaned_data['message'],
				sender = f.cleaned_data['sender']
			)
			if request.POST.has_key('send'):
				comment.save()
				return HttpResponseRedirect(a.get_absolute_url())

	else:
		f = CommentForm()

	return render_to_response(
		'news/comment/'+c.template_name, {
			'category': c,
			'article': a,
			'reply': reply,
			'comment': comment,
			'form': f,
		},
		RequestContext(request)
	)
