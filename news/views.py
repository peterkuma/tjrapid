from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils import translation

from datetime import date

from tjrapid import settings
from tjrapid.main.models import *
from models import *

def archive(request,category,lang=settings.LANGUAGE_CODE,year=None,month=None,day=None,id=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	c = Category.objects.get(language__code=lang,name=category)
	a = Article.objects.filter(category=c)
	
	if year: a = a.filter(published__year=year)
	if month: a = a.filter(published__month=month)
	if day: a = a.filter(published__day=day)	

	if month:
		if int(month) <= 12 and int(month) >= 1:
			month_name = date(1980,int(month),1).strftime('%B')
		else:
			raise Http404
	else:
		month_name = None

	location = []
	if year: location += [{ 'name': 'News', 'url': c.get_absolute_url()+'news/' }]
	if month: location += [{ 'name': year, 'url': c.get_absolute_url()+'news/'+year+'/' }]
	if day:
		location += [{ 'name': month_name, 'url': c.get_absolute_url()+'news/'+year+'/'+month+'/' }]
	
	return render_to_response(
		'news/archive/'+c.template_name, {
			'category': c,
			'articles': a,
			'location': location,
			'year': year,
			'month': month,
			'month_name': month_name,
			'day': day,
		},
		RequestContext(request)
	)

def details(request,category,lang=settings.LANGUAGE_CODE,year=None,month=None,day=None,id=None):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	try:
		c = Category.objects.get(language__code=lang,name=category)
		a = Article.objects.get(category=c,published__year=year, \
			published__month=month,published__day=day,id=id)
	except ObjectDoesNotExist:
		raise Http404

	location = (
		{ 'name': 'News', 'url': c.get_absolute_url()+'news/' },
		{ 'name': a.published.strftime('%Y'), 'url': c.get_absolute_url()+'news/'+a.published.strftime('%Y')+'/' },
		{ 'name': a.published.strftime('%B'), 'url': c.get_absolute_url()+'news/'+a.published.strftime('%Y')+'/'+a.published.strftime('%m')+'/' },
	)

	return render_to_response(
		'news/details/'+c.template_name, {
			'category': c,
			'article': a,
			'location': location,
		},
		RequestContext(request)
	)
