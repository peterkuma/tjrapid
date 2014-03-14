# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.markup.templatetags import markup
from django.template.defaultfilters import truncatewords, striptags

from main.models import Category
from news.models import Article


class NewsFeed(Feed):
    def get_object(self, request, category_name):
        self.title = _('Orienteering Club TJ Rapid')
        return get_object_or_404(Category, name=category_name)

    def link(self, obj):
        return '%snews' % obj.get_absolute_url()

#    def item_description(self, item):
#        return markup.textile(item.head)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        if item.head:
            return truncatewords(striptags(item.head_html()), 40)
        else:
            return truncatewords(striptags(item.body_html()), 40)

    def item_author(self, item):
        return item.author

    def item_pubdate(self, item):
        return item.published

    def items(self, obj):
        return Article.objects.filter(category=obj).exclude(title='')
