# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2007, 2008, 2009 2010 Peter Kuma
# All rights reserved.
#

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from news.feed import NewsFeed

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/eventapp/', include('tjrapid.eventapp.admin_urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^ob/clenovia/$','tjrapid.ob.views.members',dict(category_name='ob')),
	(r'^en/orienteering/members/$','tjrapid.ob.views.members',dict(category_name='orienteering')),
	(r'^ob/preteky/$','tjrapid.ob.views.competitions',dict(category_name='ob')),
	(r'^en/orienteering/competitions/$','tjrapid.ob.views.competitions',
	    dict(category_name='orienteering')),
	(r'^(?P<category>[^/]+)/news/',include('tjrapid.news.urls')),
	(r'^(?P<category>ob)/news/rss/', NewsFeed()),
	(r'^(?P<category>en)/orienteering/news/rss/', NewsFeed()),
	(r'^(?P<lang>[^/]+)/(?P<category>[^/]+)/news/',include('tjrapid.news.urls')),
	(r'^ob/prihlaska/', include('tjrapid.eventapp.urls', namespace='eventapp-sk', app_name='eventapp'), dict(category='ob', namespace='eventapp-sk')),
	(r'^en/orienteering/entry/', include('tjrapid.eventapp.urls', namespace='eventapp-en', app_name='eventapp'), dict(category='orienteering', namespace='eventapp-en')),
	(r'^([^/]*)/?$','tjrapid.main.views.page'),
	(r'^([^/]*)/([^/]*)/$','tjrapid.main.views.page'),
	(r'^([^/]*)/([^/]*)/([^/]*)/$','tjrapid.main.views.page'),
)
