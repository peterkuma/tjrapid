# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib import admin
from django_attach.forms import AttachmentInline
from linguo.forms import MultilingualModelForm

from news.models import *


class ArticleAdminForm(MultilingualModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title','author','published','category')
    search_fields = ('title','author','head','body')
    list_filter = ('author','category')
    inlines = (AttachmentInline,)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('subject','sender','article','ip','useragent','posted',)
    search_fields = ('subject','message','article','sender')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
