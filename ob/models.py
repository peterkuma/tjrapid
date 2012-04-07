# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from datetime import date

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from main.models import Category

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

	class Admin:
		list_display = ('surname','first_name','category','email')
		search_fields = ('first_name','surname')
		list_filter = ('category',)

class Competition(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		unique=True,
#		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL')
	)
	start_date = models.DateField(_('start date'))
	end_date = models.DateField(_('end date'),null=True,blank=True)
	location = models.CharField(_('location'),max_length=100,blank=True)
	category = models.ForeignKey(Category,verbose_name=_('category'))

#	specification = SmartFileField(_('specification'),blank=True)
#	def get_specification_relative_filename(self):
#		return 'upload/%s/%s/%s/%s.%s' % (self.category.name,_('competitions'),_('specification'),self.name,self.specification_ext())
#	def specification_ext(self):
#		return os.path.splitext(specification)[1]
#	results = models.FileField(_('results'),blank=True)
#	results = models.CharField(_('results'),max_length=200,blank=True)
#	photos = models.CharField(_('photos'),max_length=200,blank=True)

	def is_upcoming(self):
		return ((self.end_date is None and self.start_date >= date.today()) or (self.end_date is not None and self.end_date >= date.today()))

	def specification(self):
		for ext in ('pdf', 'doc', 'rtf'):
			path = 'upload/%s/%s/%s_%s.%s' % (self.category.name, _('competitions'), self.name, _('specification'), ext)
			if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
				return settings.MEDIA_URL+path
		return None

	def results(self):
		for ext in ('pdf', 'doc', 'rtf'):
			path = 'upload/%s/%s/%s_%s.%s' % (self.category.name, _('competitions'), self.name, _('results'), ext)
			if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
				return settings.MEDIA_URL+path
		return None

	def directives(self):
		for ext in ('pdf', 'doc', 'rtf'):
			path = 'upload/%s/%s/%s_%s.%s' % (self.category.name, _('competitions'), self.name, _('directives'), ext)
			if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
				return settings.MEDIA_URL+path
		return None

	class Meta:
		ordering = ('-start_date',)
		verbose_name = _('competition')
		verbose_name_plural = _('competitions')

	class Admin:
		list_display = ('title','start_date','end_date')
		search_fields = ('title','location')
		list_filter = ('start_date','location')
