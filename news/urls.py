# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('news.views',
	(r'^$','archive'),
	(r'^(?P<page>\d+)?/$','archive'),
	(r'^article/(?P<id>\d+)/$','details'),
	(r'^article/(?P<id>\d+)/(?P<attachment>[^/]+)$','attachment'),
	(r'^article/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$','comment'),
	(r'^article/(?P<id>\d+)/comment/(?P<attachment>[^/]+)$','attachment'),
	(r'^article/(?P<id>\d+)/comment/\d+/(?P<attachment>[^/]+)$','attachment'),

	# Legacy URLs.
	#(r'^(?P<year>\d{4})/$','archive'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/$','archive'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','archive'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$','details'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$','comment'),
	(r'^\d{4}/$','archive'),
	(r'^\d{4}/\d{2}/$','archive'),
	(r'^\d{4}/\d{2}/\d{2}/$','archive'),
	(r'^\d{4}/\d{2}/\d{2}/(?P<id>\d+)/$','details'),
	(r'^\d{4}/\d{2}/\d{2}/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$','comment'),
)
