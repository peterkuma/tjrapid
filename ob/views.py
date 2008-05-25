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

