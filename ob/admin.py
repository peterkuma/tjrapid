# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django import forms
from django.contrib import admin
from django_attach.forms import AttachmentInline
from linguo.forms import MultilingualModelForm

from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ('surname','first_name','category','email')
    search_fields = ('first_name','surname')
    list_filter = ('category',)


class MarkerSelectWidget(forms.widgets.Select):
    template_name = 'ob/marker_select.html'
    option_template_name = 'ob/marker_select_option.html'


class MapPointForm(forms.ModelForm):
    model = MapPoint
    class Meta:
        widgets = {
            'marker': MarkerSelectWidget
        }


class MapPointInline(admin.StackedInline):
    form = MapPointForm
    model = MapPoint
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','start_date','end_date')
    search_fields = ('title','location')
    list_filter = ('start_date','location')
    inlines = (MapPointInline, AttachmentInline,)


admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
