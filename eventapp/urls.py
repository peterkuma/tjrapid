# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.urls import *
from django.conf import settings
import eventapp.views

urlpatterns = [
	re_path(r'^(?P<id>EV\d{4}-\d{4})/$',eventapp.views.event, name='event'),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<id>ER\d{4}-\d{4})/$',eventapp.views.entry, name='entry'),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<id>ER\d{4}-\d{4})/pdf/$',eventapp.views.entry_pdf, name='entry-pdf'),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/action/$',eventapp.views.action),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/list/$',eventapp.views.list),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/list/$',eventapp.views.list),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/PA/$',eventapp.views.participant, name='new-participant'),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/(?P<id>PA\d{4}-\d{4})/$',eventapp.views.participant, name='participant'),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/PA/search/$',eventapp.views.query),
	re_path(r'^(?P<eventid>EV\d{4}-\d{4})/(?P<entryid>ER\d{4}-\d{4})/(?P<id>PA\d{4}-\d{4})/search/$',eventapp.views.query),
]
