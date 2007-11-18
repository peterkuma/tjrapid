# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

from tjrapid import settings

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
	
	class Admin:
		pass

class Category(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
	language = models.ForeignKey(Language,verbose_name=_('language'))
	template_name = models.CharField(_('template name'),max_length=100)
	menu = models.TextField(_('menu'),blank=True)

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
	
	path.short_description = _('path')
	
	class Meta:
		ordering = ['title']
		verbose_name = _('category')
		verbose_name_plural = _('categories')
	
	class Admin:
		list_display = ('title','path','language')
		list_filter = ('language',)

class Page(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		blank=True,
		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL'),
	)
	category = models.ForeignKey(Category,verbose_name=_('category'))
	content = models.TextField(_('content'),blank=True)
	created = models.DateTimeField(_('created'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)

	def __unicode__(self):
		return '%s -- %s' % (self.category.title, self.title)

	def path(self):
		if(self.name == ''):
			return self.category.path()
		else:
			return '%s%s/' % (self.category.path(), self.name)

	path.short_description = _('path')

	class Meta:
		get_latest_by = 'modified',
		ordering = ('category','title')
		unique_together = (('name','category'),)
		verbose_name = _('page')
		verbose_name_plural = _('pages')
	
	class Admin:
		list_display = ('title','category','path','created','modified')
		search_fields = ('name','title')
		list_filter = ('category',)
		js = ('/site_media/admin.js',)

