# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.shortcuts import render_to_response, get_object_or_404
from django.utils import translation

from models import *

class LanguageMiddleware(object):
	def process_view(self, request, view_func, view_args, view_kwargs):
		if view_kwargs.has_key('lang'):
			translation.activate(view_kwargs['lang'])
			request.LANGUAGE_CODE = translation.get_language()

class CategoryMiddleware(object):
	def process_view(self, request, view_func, view_args, view_kwargs):
		if view_kwargs.has_key('category'):
			c = get_object_or_404(Category,  name=view_kwargs['category'])
			translation.activate(c.language.code)
			request.LANGUAGE_CODE = translation.get_language()
			request.category = c
