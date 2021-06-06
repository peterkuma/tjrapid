# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
import django.views.static

import ob.views
from ob.news import OrienteeringNews

admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
	urlpatterns += [
		re_path(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
	]
elif settings.SERVE_STATIC:
	urlpatterns += [
		re_path(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
		re_path(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
	]

urlpatterns += [
	re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	re_path(r'^admin/eventapp/', include('eventapp.admin_urls')),
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^ob/clenovia/$',ob.views.members,kwargs=dict(category_name='ob')),
	re_path(r'^(?P<lang>en)/orienteering/members/$',ob.views.members, kwargs=dict(category_name='orienteering')),
	re_path(r'^(?P<category_name>ob)/preteky/$', ob.views.events, kwargs={'lang': 'sk'}),
	re_path(r'^(?P<category_name>ob)/preteky/(?P<name>[^/]+)/$', ob.views.event, kwargs={'lang': 'sk'}),
	re_path(r'^(?P<category_name>ob)/preteky/(?P<event_name>[^/]+)/(?P<name>[^/]+)$', ob.views.attachment),
	re_path(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/$', ob.views.events),
	re_path(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/(?P<name>[^/]+)/$', ob.views.event),
	re_path(r'^(?P<lang>en)/(?P<category_name>orienteering)/events/(?P<event_name>[^/]+)/(?P<name>[^/]+)$', ob.views.attachment),
	re_path(r'^(?P<category_name>ob)/$', RedirectView.as_view(url='/ob/news/')),
	re_path(r'^en/(?P<category_name>orienteering)/$', RedirectView.as_view(url='/en/orienteering/news/')),
	re_path(r'^(?P<category_name>ob)/news/', include(OrienteeringNews('news-sk').urls, namespace='news-sk')),
	re_path(r'^en/(?P<category_name>orienteering)/news/', include(OrienteeringNews('news-en').urls, namespace='news-en'), kwargs={'lang': 'en'}),
	re_path(r'^ob/prihlaska/', include(('eventapp.urls', 'eventapp'), namespace='eventapp-sk'), kwargs=dict(category='ob', namespace='eventapp-sk')),
	re_path(r'^en/orienteering/entry/', include(('eventapp.urls', 'eventapp'), namespace='eventapp-en'), kwargs=dict(category='orienteering', namespace='eventapp-en')),
	re_path(r'^(?P<lang>en)/', include(('main.urls', 'main'), namespace='main-en'), kwargs={'lang': 'en'}),
	re_path(r'', include(('main.urls', 'main'), namespace='main-sk')),
]
