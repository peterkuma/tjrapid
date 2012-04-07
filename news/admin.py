# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from attachment.models import Attachment
from models import *

class AttachmentInline(GenericTabularInline):
	model = Attachment
	extra = 2

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','author','published','category')
	search_fields = ('title','author','head','body')
	list_filter = ('author','category')
	fields = ('title', 'author', 'category', 'head', 'body')
	inlines = (AttachmentInline,)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('subject','sender','article','posted',)
	search_fields = ('subject','message','article','sender')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
