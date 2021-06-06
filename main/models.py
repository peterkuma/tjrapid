# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.safestring import mark_safe
from markdown import markdown
from textile import textile
from django.conf import settings
from django.utils.translation import get_language
from django_attach.models import Attachment
from linguo.models import MultilingualModel
from linguo.managers import MultilingualManager


MARKUP_CHOICES = (
	('markdown', 'Markdown'),
	('textile', 'Textile'),
	('html', 'HTML'),
)


class Category(MultilingualModel):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
#		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
	template_name = models.CharField(_('template name'),max_length=100)
	markup = models.CharField(
		_('markup'),
		max_length=50,
		choices=MARKUP_CHOICES,
		default='markdown',
		help_text=_('Documentation: <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a>, <a href="http://en.wikipedia.org/wiki/Textile_(markup_language)">Textile</a>')
	)
	menu = models.TextField(_('menu'),blank=True)
	attachments = GenericRelation(Attachment)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		lang = get_language()
		if lang == settings.LANGUAGE_CODE:
			return os.path.join('/', self.name+'/')
		else:
			return os.path.join('/', lang, self.name+'/')

	def path(self):
		return self.get_absolute_url()

	def menu_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.menu))
		elif self.markup == 'textile': return mark_safe(textile(self.menu))
		else: return mark_safe(self.menu)

	path.short_description = _('path')

	class Meta:
		ordering = ['title']
		verbose_name = _('category')
		verbose_name_plural = _('categories')
		translate = ('title', 'name', 'menu')


class Page(MultilingualModel):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
#		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
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
	content = models.TextField(_('content'),blank=True,help_text=_('Add files and images below'))
	created = models.DateTimeField(_('created'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)
	attachments = GenericRelation(Attachment)
	style = models.TextField(_('style'),blank=True,help_text=_('Cascading Style Sheets'))

	def __unicode__(self):
		return u'%s -- %s' % (self.category.title, self.title)

	def path(self):
		if(self.name == ''):
			return self.category.path()
		else:
			return '%s%s/' % (self.category.path(), self.name)

	def content_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.content))
		elif self.markup == 'textile': return mark_safe(textile(self.content))
		else: return mark_safe(self.content)

	path.short_description = _('path')

	objects = MultilingualManager()

	class Meta:
		get_latest_by = 'modified',
		ordering = ('category','name')
		unique_together = (('name','category'),)
		verbose_name = _('page')
		verbose_name_plural = _('pages')
		translate = ('title', 'name', 'content')
