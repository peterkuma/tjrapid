# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2007, 2008, 2009, 2010 Peter Kuma
# All rights reserved.
#

import os

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from django.http import HttpResponseRedirect

from tjrapid import settings
from tjrapid.main.models import Page

def page(request, path=''):
	path = '/' + path
	pages = Page.objects.all()
	for p in pages:
		if p.path() == path:
			translation.activate(p.category.language.code)
			request.LANGUAGE_CODE = translation.get_language()
			return render_to_response(p.category.template_name, {
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
