# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

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
	(r'^(?P<lang>en)/orienteering/members/$','ob.views.members',dict(category_name='orienteering')),
	url(r'^(?P<category_name>ob)/preteky/$', 'ob.views.events'),
	url(r'^(?P<category_name>ob)/preteky/(?P<name>[^/]+)/$', 'ob.views.event'),
	url(r'^(?P<category_name>ob)/preteky/(?P<event_name>[^/]+)/(?P<name>[^/]+)$', 'ob.views.attachment'),
	url(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/$', 'ob.views.events'),
	url(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/(?P<name>[^/]+)/$', 'ob.views.event'),
	url(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/(?P<event_name>[^/]+)/(?P<name>[^/]+)$', 'ob.views.attachment'),
	url(r'^(?P<category_name>ob)/$', RedirectView.as_view(url='/ob/news/')),
	url(r'^en/(?P<category_name>orienteering)/$', RedirectView.as_view(url='/en/orienteering/news/')),
	url(r'^(?P<category_name>ob)/news/', include('news.urls', namespace='news-sk', app_name='news')),
	url(r'^en/(?P<category_name>orienteering)/news/', include('news.urls', namespace='news-en', app_name='news'), kwargs={'lang': 'en'}),
	(r'^ob/prihlaska/', include('eventapp.urls', namespace='eventapp-sk', app_name='eventapp'), dict(category='ob', namespace='eventapp-sk')),
	(r'^en/orienteering/entry/', include('eventapp.urls', namespace='eventapp-en', app_name='eventapp'), dict(category='orienteering', namespace='eventapp-en')),
	url(r'^(?P<lang>en)/', include('main.urls', namespace='main'), kwargs={'lang': 'en'}),
	url(r'', include('main.urls', namespace='main')),
)
