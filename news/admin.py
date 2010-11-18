# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from models import *
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','category','path','published','author','modified')
	search_fields = ('name','title','head','body')
	list_filter = ('category','published','author')

class CommentAdmin(admin.ModelAdmin):
		list_display = ('subject','article','reply','posted','sender')
		search_fields = ('subject','message','article','sender')
		list_filter = ('posted',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

