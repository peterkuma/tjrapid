# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.markup.templatetags import markup

from main.models import Category
from models import Article

class NewsFeed(Feed):
    def get_object(self, request, category, title):
        self.title = title
        return get_object_or_404(Category, name=category)

    def link(self, obj):
        return '%snews' % obj.get_absolute_url()

#    def item_description(self, item):
#        return markup.textile(item.head)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return None

    def item_author(self, item):
        return item.author

    def item_pubdate(self, item):
        return item.published

    def items(self, obj):
        return Article.objects.filter(category=obj)
