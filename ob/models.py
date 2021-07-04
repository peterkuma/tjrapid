# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from datetime import date, datetime
import urllib.request, urllib.error, urllib.parse
import json
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from markdown import markdown
from textile import textile
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.fields import GenericRelation
from django_attach.models import Attachment
from linguo.models import MultilingualModel
from linguo.managers import MultilingualManager
from django.urls import reverse
from django.utils.translation import get_language

from main.models import Category


MARKUP_CHOICES = (
	('markdown', 'Markdown'),
	('textile', 'Textile'),
	('html', 'HTML'),
)


class Member(models.Model):
	first_name = models.CharField(_('first name'), max_length=50)
	surname = models.CharField(_('surname'), max_length=50)
	category = models.CharField(_('category'), max_length=5)
	email = models.EmailField(_('e-mail'), blank=True)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.surname)

	def email_special(self):
		return self.email.replace('@', '[zavinac]')

	class Meta:
		ordering = ('category','surname')
		verbose_name = _('member')
		verbose_name_plural = _('members')


class Event(MultilingualModel):
	title = models.CharField(_('title'), max_length=100)
	name = models.SlugField(
		_('name'),
		unique=True,
		help_text=_('Short name that will appear in the URL')
	)
	start_date = models.DateField(_('start date'))
	end_date = models.DateField(_('end date'), null=True, blank=True)
	location = models.CharField(_('location'), max_length=100)
	latitude = models.FloatField(_('latitude'), null=True, blank=True)
	longitude = models.FloatField(_('longitude'), null=True, blank=True)
	category = models.ForeignKey(Category,
		verbose_name=_('category'),
		on_delete=models.CASCADE,
	)
	markup = models.CharField(
		_('markup'),
		max_length=50,
		choices=MARKUP_CHOICES,
		default='markdown',
		help_text=_('Documentation: <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a>, <a href="http://en.wikipedia.org/wiki/Textile_(markup_language)">Textile</a>')
	)
	head = models.TextField(
		_('head'),
		blank=True,
		help_text=_('Add files and images below')
	)
	body = models.TextField(
		_('body'),
		blank=True,
		help_text=_('Add files and images below')
	)
	attachments = GenericRelation(Attachment)
	created = models.DateTimeField(_('created'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)

	def get_absolute_url(self):
		import ob.views
		return reverse(ob.views.event, kwargs={
			'lang': get_language(),
			'category_name': Category.objects.get(name_en='orienteering').name,
			'name': self.name,
		})

	def head_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.head))
		elif self.markup == 'textile': return mark_safe(textile(self.head))
		else: return mark_safe(self.head)

	def body_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.body))
		elif self.markup == 'textile': return mark_safe(textile(self.body))
		else: return mark_safe(self.body)

	def is_upcoming(self):
		return self.end_date is None and self.start_date >= date.today() or \
			   self.end_date is not None and self.end_date >= date.today()

	objects = MultilingualManager()

	class Meta:
		ordering = ('-start_date',)
		verbose_name = _('event')
		verbose_name_plural = _('events')
		translate = ('title', 'name', 'location', 'head', 'body')
