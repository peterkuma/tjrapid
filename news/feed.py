# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.markup.templatetags import markup

from models import Article
from tjrapid.main.models import Category

class NewsFeed(Feed):
    link = 'ob/news'
    
    def get_object(self, request, category):
        return get_object_or_404(Category, name=category)
    
    def title(self, obj):
        return _('News for %s') % obj.title
        
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
        return Article.objects.filter(category=obj)[:5]
