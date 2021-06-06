# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Peter Kuma

from django.urls import *
from django.conf import settings

from .admin_views import *

urlpatterns = [
	#re_path(r'^event/(?P<id>EV\d{4}-\d{4})/(?P<format>csv)/report/$', report),
	re_path(r'^event/(?P<id>EV\d{4}-\d{4})/(?P<format>csv)/fullreport/$', report, dict(full=True)),
]
