# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.contrib import admin
from django.utils.translation import ugettext as _
from django_attach.forms import AttachmentInline
from linguo.forms import MultilingualModelForm

from main.models import *


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','path')
	inlines = (AttachmentInline,)


class PageAdminForm(MultilingualModelForm):
    class Meta:
        model = Page


class PageAdmin(admin.ModelAdmin):
	form = PageAdminForm
	list_display = ('title','category','path')
	search_fields = ('name','title')
	list_filter = ('category',)
	inlines = (AttachmentInline,)

	fieldsets = (
		(None, { 'fields': (
				'title',
				'title_en',
				'name',
				'name_en',
				'category',
				'markup',
				'content',
				'content_en',
		)}),
		(_('Advanced options'), {
			'classes': ('collapse',),
			'fields': ('style',)
		}),
	)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
