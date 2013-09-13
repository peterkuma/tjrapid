# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.generic import GenericRelation

from django.conf import settings
from django_attach.models import Attachment

from django.contrib.markup.templatetags.markup import markdown, textile

MARKUP_CHOICES = (
	('markdown', 'Markdown'),
	('textile', 'Textile'),
	('html', 'HTML'),
)

class Language(models.Model):
	code = models.CharField(_('code'),unique=True,
		max_length=20,
		help_text=_('All choices can be found here: http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes')
	)
	name = models.CharField(_('name'),max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['code']
		verbose_name = _('language')
		verbose_name_plural = _('languages')


class Category(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
#		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
	language = models.ForeignKey(Language,verbose_name=_('language'))
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
		return '%s (%s)' % (self.title,self.language.code)

	def get_absolute_url(self):
		path = '/'
		if self.language.code != settings.LANGUAGE_CODE:
			path += self.language.code+'/'
		if self.name != '':
			path += self.name+'/'
		return path

	def path(self):
		return self.get_absolute_url()

	def menu_html(self):
		if self.markup == 'markdown': return markdown(self.menu)
		elif self.markup == 'textile': return textile(self.menu)
		else: return self.menu

	path.short_description = _('path')

	class Meta:
		ordering = ['title']
		verbose_name = _('category')
		verbose_name_plural = _('categories')


class Page(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
#		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
	category = models.ForeignKey(Category,verbose_name=_('category'))
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
		if self.markup == 'markdown': return markdown(self.content)
		elif self.markup == 'textile': return textile(self.content)
		else: return self.content

	path.short_description = _('path')

	class Meta:
		get_latest_by = 'modified',
		ordering = ('category','name')
		unique_together = (('name','category'),)
		verbose_name = _('page')
		verbose_name_plural = _('pages')
