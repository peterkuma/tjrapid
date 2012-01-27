# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from models import *
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from tjrapid.attachment.models import Attachment

class AttachmentInline(GenericTabularInline):
	model = Attachment
	extra = 2

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','category','path','published','author','modified')
	search_fields = ('title','author','head','body')
	list_filter = ('category','published','author')
	fields = ('title', 'author', 'category', 'head', 'body')
	inlines = (AttachmentInline,)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('subject','article','reply','posted','sender')
	search_fields = ('subject','message','article','sender')
	list_filter = ('posted',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

