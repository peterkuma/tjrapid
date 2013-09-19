# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.shortcuts import render_to_response, get_object_or_404
from django.utils import translation
from django.conf import settings

from models import *

class LanguageMiddleware(object):
	def process_view(self, request, view_func, view_args, view_kwargs):
		lang = view_kwargs.get('lang', settings.LANGUAGE_CODE)
		translation.activate(lang)
		request.LANGUAGE_CODE = translation.get_language()
		try: del view_kwargs['lang']
		except KeyError: pass
