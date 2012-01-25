# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2012 Peter Kuma
# All rights reserved.
#

from models import *
from django.contrib import admin

class AttachmentAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'content_type', 'object_id', 'content_object')
	list_filter = ('content_type',)

admin.site.register(Attachment, AttachmentAdmin)
