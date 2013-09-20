# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from main.models import *
from ob.models import *


def events(request, category_name):
	category = get_object_or_404(Category, name=category_name)
	events = Event.objects.filter(category=category)
	return render_to_response(
		'ob/events.html', {
			'events': events,
			'category': category,
		},
		RequestContext(request)
	)


def event(request, name, category_name):
	category = get_object_or_404(Category, name=category_name)
	event = get_object_or_404(Event, category=category, name=name)
	return render_to_response(
		'ob/event.html', {
			'event': event,
			'category': category,
		},
		RequestContext(request)
	)


def attachment(request, category_name, event_name, name):
	category = get_object_or_404(Category, name=category_name)
	event = get_object_or_404(Event, category=category, name=event_name)
	for a in event.attachments.all():
		if os.path.basename(a.file.name) == name:
			return HttpResponseRedirect(a.file.url)
	raise Http404	


def members(request, category_name):
	members_m = Member.objects.filter(category__startswith='M')
	members_w = Member.objects.filter(category__startswith='W')
	category = Category.objects.get(name=category_name)

	return render_to_response(
		'ob/members.html', {
			'members_m': members_m,
			'members_w': members_w,
			'category': category,
		},
		RequestContext(request)
	)
