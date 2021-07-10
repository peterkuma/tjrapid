# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os

from django.http import Http404
from django.shortcuts import render
from django.template import RequestContext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from main.models import Category, Page


def page(request, category_name, name):
	p = get_object_or_404(Page, category__name=category_name, name=name)
	if p.redirect and ( \
		p.redirect.startswith('http://') or \
		p.redirect.startswith('https://') \
	):
		return redirect(p.redirect)
	return render(request, 'main/' + p.category.template_name, {
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
