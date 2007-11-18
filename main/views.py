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

