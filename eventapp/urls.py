# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('eventapp.views',
	url(r'^(?P<id>EV\d{4}-\d{4})/$','event', name='event'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<id>ER\d{4}-\d{4})/$','entry', name='entry'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<id>ER\d{4}-\d{4})/pdf/$','entry_pdf', name='entry-pdf'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/action/$','action'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/list/$','list'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/list/$','list'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/PA/$','participant', name='new-participant'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/(?P<id>PA\d{4}-\d{4})/$','participant', name='participant'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/PA/search/$','query'),
	url(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/(?P<id>PA\d{4}-\d{4})/search/$','query'),
)
