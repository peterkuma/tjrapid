# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib import admin
from django_attach.forms import AttachmentInline

from .models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ('surname','first_name','category','email')
    search_fields = ('first_name','surname')
    list_filter = ('category',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','start_date','end_date')
    search_fields = ('title','location')
    list_filter = ('start_date','location')
    inlines = (AttachmentInline,)

admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
