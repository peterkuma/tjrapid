# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Peter Kuma

from django.contrib import admin

from models import *

class AttachmentAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'content_type', 'object_id', 'content_object')
	list_filter = ('content_type',)

admin.site.register(Attachment, AttachmentAdmin)
