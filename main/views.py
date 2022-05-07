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
	categories = Category.objects.all()
	return render(request, 'main/' + p.category.template_name, {
					'page': p,
					'category': p.category,
					'style': p.style,
					'categories': categories,
	}, RequestContext(request))

def attachment(request, category_name, page_name, name):
	def redirect_or_404():
		if not request.path.endswith('/'):
			return HttpResponseRedirect(request.path + '/')
		raise Http404
		
	if page_name == '':
		try:
			c = Category.objects.get(name=category_name)
		except Category.DoesNotExist:
			return redirect_or_404()
		for a in c.attachments.all():
			if os.path.basename(a.file.name) == name:
				return HttpResponseRedirect(a.file.url)

	try:
		p = Page.objects.get(
			category__name=category_name,
			name=page_name
		)
	except Page.DoesNotExist:
		return redirect_or_404()

	for a in p.attachments.all():
		if os.path.basename(a.file.name) == name:
			return HttpResponseRedirect(a.file.url)
	return redirect_or_404()
