# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Peter Kuma

from django.conf.urls.defaults import *
from django.conf import settings

from admin_views import *

urlpatterns = patterns('',
	#url(r'^event/(?P<id>EV\d{4}-\d{4})/(?P<format>csv)/report/$', report),
	url(r'^event/(?P<id>EV\d{4}-\d{4})/(?P<format>csv)/fullreport/$', report, dict(full=True)),
)
