# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2007, 2008, 2009 2010 Peter Kuma
# All rights reserved.
#

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('tjrapid.news.views',
	(r'^$','archive'),
	(r'^(?P<year>\d{4})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$','details'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/comment/(?P<reply_id>\d+)?/?$','comment'),
)
