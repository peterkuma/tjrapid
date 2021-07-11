# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib.syndication.views import Feed, FeedDoesNotExist, add_domain
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from django.template.defaultfilters import truncatewords, striptags
from django.utils.feedgenerator import DefaultFeed
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

from main.models import Category
from news.models import Article


class NewsFeed(Feed):
    def feed(self, request, category_name):
        c = get_object_or_404(Category, name=category_name)
        current_site = get_current_site(request)
        link = add_domain(
            current_site.domain,
            self.link(c) + '/rss/',
            request.is_secure()
        )
        return render(request, 'news/feed.html', {
            'link': link,
        })

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
