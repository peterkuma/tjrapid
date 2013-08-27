# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from django.utils.translation import ugettext as _

from models import *
from attachment.models import Attachment

class AttachmentInline(GenericTabularInline):
	model = Attachment
	extra = 2

class LanguageAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','path','language')
	list_filter = ('language',)
	inlines = (AttachmentInline,)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','path')
	search_fields = ('name','title')
	list_filter = ('category',)
	inlines = (AttachmentInline,)

	fieldsets = (
		(None, {'fields': ('title', 'name', 'category', 'markup', 'content')}),
		(_('Advanced options'), {
			'classes': ('collapse',),
			'fields': ('style',)
		}),
	)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
