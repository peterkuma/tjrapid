# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2007, 2008, 2009 2010 Peter Kuma
# All rights reserved.
#

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation

from datetime import datetime

from tjrapid.main.models import *
from models import *

def competitions(request, category_name):
	competitions = Competition.objects.all()
	competitions_upcoming = filter(lambda c: c.is_upcoming(), competitions)
	competitions_past = filter(lambda c: not c.is_upcoming(), competitions)
	category = Category.objects.get(name=category_name)
	
	translation.activate(category.language.code)
	request.LANGUAGE_CODE = translation.get_language()
	
	return render_to_response(
		'ob_competitions.html', {
			'competitions_upcoming': competitions_upcoming,
			'competitions_past': competitions_past,
			'category': category,
		},
		RequestContext(request)
	)
def members(request, category_name):
	members_m = Member.objects.filter(category__startswith='M')
	members_w = Member.objects.filter(category__startswith='W')
	category = Category.objects.get(name=category_name)
	
	translation.activate(category.language.code)
	request.LANGUAGE_CODE = translation.get_language()
	
	return render_to_response(
		'ob_members.html', {
			'members_m': members_m,
			'members_w': members_w,
			'category': category,
		},
		RequestContext(request)
	)

