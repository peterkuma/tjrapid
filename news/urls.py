# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.conf.urls.defaults import *
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from news.feed import NewsFeed


urlpatterns = patterns('news.views',
	url(r'^$','archive'),
	url(r'^(?P<page>\d+)?/$','archive', name='archive'),
	url(r'^article/(?P<id>\d+)/$','detail', name='detail'),
	url(r'^article/(?P<id>\d+)/(?P<name>[^/]+)$', 'attachment', name='attachment'),
	url(r'^article/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$', 'comment', name='comment'),
	url(r'^rss/$', NewsFeed(), name='rss'),
    url(r'^rss/feed.xsl$', TemplateView.as_view(template_name='news/feed.xsl'))
)
