# -*- coding: utf-8 -*-

# $Id$

# Copyright (c) 2007, 2008, Peter Kuma
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of TJ Rapid nor the names of its contributors may be used
#    to endorse or promote products derived from this software without
#    specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils import translation
from tjrapid import settings
from tjrapid.main.models import Page

def page(request, *args):
	p = None

	if len(args) == 1:
		# /lang/
		try:
			p = Page.objects.get(category__language__code=args[0],category__name='',name='')
		except ObjectDoesNotExist:
			pass

		# /page/
		try:
			p = Page.objects.get(category__language__code=settings.LANGUAGE_CODE,category__name='',name=args[0])
		except ObjectDoesNotExist:
			pass

		# /category/
		try:
			p = Page.objects.get(category__language__code=settings.LANGUAGE_CODE,category__name=args[0],name='')
		except ObjectDoesNotExist:
			pass

	if len(args) == 2:
		# /lang/page/
		try:
			p = Page.objects.get(category__language__code=args[0],category__name='',name=args[1])
		except ObjectDoesNotExist:
			pass

		# /lang/category/
		try:
			p = Page.objects.get(category__language__code=args[0],category__name=args[1],name='')
		except ObjectDoesNotExist:
			pass

		# /category/page/
		try:
			p = Page.objects.get(category__language__code=settings.LANGUAGE_CODE,category__name=args[0],name=args[1])
		except ObjectDoesNotExist:
			pass

	if len(args) == 3:
		# /lang/category/page/
		try:
			p = Page.objects.get(category__language__code=args[0],category__name=args[1],name=args[2])
		except ObjectDoesNotExist:
			pass
	
	if p is None:
		raise Http404

	translation.activate(p.category.language.code)
	request.LANGUAGE_CODE = translation.get_language()

	return render_to_response(
		p.category.template_name, {
			'page': p,
			'category': p.category,
		},
		RequestContext(request)
	)

