# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings

from main.models import Page

def page(request, path=''):
	path = '/' + path
	pages = Page.objects.all()
	for p in pages:
		if p.path() == path:
			translation.activate(p.category.language.code)
			request.LANGUAGE_CODE = translation.get_language()
			return render_to_response('main/'+p.category.template_name, {
					'page': p,
					'category': p.category,
					'style': p.style
				}, RequestContext(request))
	raise Http404

def attachment(request, path):
	page_path = '/' + os.path.dirname(path) + '/'
	attachment = os.path.basename(path)

	pages = Page.objects.all()
	for p in pages:
		if p.path() == page_path:
			for a in p.attachments.all() | p.category.attachments.all():
				if os.path.basename(a.file.name) == attachment:
					return HttpResponseRedirect(a.file.url)

	raise Http404
