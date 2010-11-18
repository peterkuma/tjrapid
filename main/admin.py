# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from models import *
from django.contrib import admin

class LanguageAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','path','language')
	list_filter = ('language',)
	
class ClassFeeAdmin(admin.ModelAdmin):
	list_display = ('event', 'label', 'classes')
	list_filter = ('event',)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','path','created','modified')
	search_fields = ('name','title')
	list_filter = ('category',)
	js = ('/site_media/admin.js',)

admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

