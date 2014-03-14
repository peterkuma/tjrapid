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
from django.shortcuts import get_object_or_404

from main.models import Category, Page


def page(request, category_name, name):
	p = get_object_or_404(Page, category__name=category_name, name=name)
	return render_to_response('main/' + p.category.template_name, {
					'page': p,
					'category': p.category,
					'style': p.style
	}, RequestContext(request))


def attachment(request, category_name, page_name, name):
	if page_name == '':
		c = get_object_or_404(Category, name=category_name)
		for a in c.attachments.all():
			if os.path.basename(a.file.name) == name:
				return HttpResponseRedirect(a.file.url)

	p = get_object_or_404(Page,
		category__name=category_name,
		name=page_name
	)

	for a in p.attachments.all():
		if os.path.basename(a.file.name) == name:
			return HttpResponseRedirect(a.file.url)
	raise Http404
