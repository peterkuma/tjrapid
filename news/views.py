# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from datetime import date

from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

from main.models import *
from models import *

def archive(request, category, page=None):
	c = Category.objects.get(name=category)
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

def details(request, category,id=None):
	try:
		c = Category.objects.get(name=category)
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

def attachment(request,category,id=None,attachment=None):
	try:
		c = Category.objects.get(name=category)
		article = Article.objects.get(category=c,id=id)
		for a in article.attachments.all():
			if os.path.basename(a.file.name) == attachment:
				return HttpResponseRedirect(a.file.url)
	except ObjectDoesNotExist:
		raise Http404
	raise Http404

def comment(request,category,id=None,reply_id=None):
	try:
		c = Category.objects.get(name=category)
		a = Article.objects.get(category=c,id=id)
	except ObjectDoesNotExist:
		raise Http404

	if not a.comments_enabled():
		raise PermissionDenied()

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
				sender = f.cleaned_data['sender'],
				ip = request.META.get('REMOTE_ADDR'),
				useragent = request.META.get('HTTP_USER_AGENT'),
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
