# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

from news.feed import NewsFeed

admin.autodiscover()

urlpatterns = patterns('')

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
elif settings.SERVE_STATIC:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)

urlpatterns += patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/eventapp/', include('eventapp.admin_urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^ob/clenovia/$','ob.views.members',dict(category_name='ob')),
	(r'^en/orienteering/members/$','ob.views.members',dict(category_name='orienteering')),
	#(r'^ob/preteky/$','ob.views.competitions',dict(category_name='ob')),
	#(r'^en/orienteering/competitions/$','ob.views.competitions',
	#    dict(category_name='orienteering')),
	(r'^(?P<category>[^/]+)/news/',include('news.urls')),
	(r'^(?P<category>ob)/news/rss/', NewsFeed(), dict(title=u'Oddiel orientačného behu TJ Rapid')),
	(r'^(?P<category>en)/orienteering/news/rss/', NewsFeed(), dict(title='Orienteering Club TJ Rapid')),
	(r'^(?P<lang>[^/]+)/(?P<category>[^/]+)/news/',include('news.urls')),
	(r'^ob/prihlaska/', include('eventapp.urls', namespace='eventapp-sk', app_name='eventapp'), dict(category='ob', namespace='eventapp-sk')),
	(r'^en/orienteering/entry/', include('eventapp.urls', namespace='eventapp-en', app_name='eventapp'), dict(category='orienteering', namespace='eventapp-en')),
	(r'^$','main.views.page'),
	(r'^(.*/)$','main.views.page'),
	(r'^(.*[^/])$','main.views.attachment'),
)
