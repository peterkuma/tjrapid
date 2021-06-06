# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from datetime import date

from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from main.models import *
from news.models import *


class News(object):
	app_name = 'news'
	name = 'news'

	def __init__(self, name=None):
		if name is not None:
			self.name = name

	@property
	def urls(self):
		return self.get_urls(), self.app_name

	def get_urls(self):
		from django.urls import re_path, include
		from functools import partial
		from django.views.generic import TemplateView
		from news.feed import NewsFeed

		def wrap(f):
			return f

		return [
			re_path(r'^$', wrap(self.archive)),
			re_path(r'^(?P<page>\d+)?/$', wrap(self.archive), name='archive'),
			re_path(r'^article/(?P<id>\d+)/$', wrap(self.detail), name='detail'),
			re_path(r'^article/(?P<id>\d+)/(?P<name>[^/]+)$', wrap(self.attachment), name='attachment'),
			re_path(r'^article/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$', wrap(self.comment), name='comment'),
			re_path(r'^rss/$', NewsFeed(), name='rss'),
			re_path(r'^rss/feed.xsl$', TemplateView.as_view(template_name='news/feed.xsl'))
		]

	def archive(self, request, category_name, page=None):
		from django.utils import translation
		c = get_object_or_404(Category, name=category_name)
		articles_all = Article.objects.filter(category=c).exclude(title='')
		p = Paginator(articles_all, 6)

		try:
			articles = p.page(page if page else 1)
		except (EmptyPage, InvalidPage):
			articles = p.page(1)

		return TemplateResponse(request, 'news/archive/' + c.template_name, {
				'category': c,
				'articles': articles,
			},
		)

	def detail(self, request, category_name, id=None):
		c = get_object_or_404(Category, name=category_name)
		a = get_object_or_404(Article, pk=id, category=c)

		if a.title == '':
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

		return render_to_response(request, 'news/details/' + c.template_name, {
				'category': c,
				'article': a,
				'comments': comments,
			},
			RequestContext(request)
		)

	def attachment(self, request, category_name, id, name):
		article = get_object_or_404(Article, pk=id, category__name=category_name)

		if article.title == '':
			raise Http404

		for a in article.attachments.all():
			if os.path.basename(a.file.name) == name:
				return HttpResponseRedirect(a.file.url)
		raise Http404

	def comment(self, request, category_name, id, reply_id=None):
		c = get_object_or_404(Category, name=category_name)
		a = get_object_or_404(Article, pk=id, category=c)

		if a.title == '':
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

		return render_to_response(request,
			'news/comment/'+c.template_name, {
				'category': c,
				'article': a,
				'reply': reply,
				'comment': comment,
				'form': f,
			},
			RequestContext(request)
		)
