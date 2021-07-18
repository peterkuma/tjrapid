# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.utils import translation
from django.conf import settings

from .models import *

class LanguageMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		lang = view_kwargs.get('lang', settings.LANGUAGE_CODE)
		translation.activate(lang)
		request.LANGUAGE_CODE = translation.get_language()
		try: del view_kwargs['lang']
		except KeyError: pass
		if 'category_name' in view_kwargs:
			try:
				request.category = Category.objects.get(name=view_kwargs['category_name'])
			except:
				request.category = None
