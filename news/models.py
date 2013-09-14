# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from datetime import timedelta, datetime
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.generic import GenericRelation
from django.utils.safestring import mark_safe

from django_attach.models import Attachment
from main.models import *


MARKUP_CHOICES = (
	('markdown', 'Markdown'),
	('textile', 'Textile'),
	('html', 'HTML'),
)


class Article(models.Model):
	title = models.CharField(_('title'),max_length=100)
	category = models.ForeignKey(Category,verbose_name=_('category'))
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
	author = models.CharField(_('author'),max_length=100)
	published = models.DateTimeField(_('published'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)
	attachments = GenericRelation(Attachment)
	close_comments_after = models.IntegerField(
		_('close comments after (days)'),
		default=90,
		blank=True,
		null=True,
	)

	def get_absolute_url(self):
		return '%snews/article/%s/' % (self.category.get_absolute_url(), self.id)

	def path(self):
		return self.get_absolute_url()

	path.short_description = _("path")

	def __unicode__(self):
		return u'%s -- %s' % (self.category,self.title)

	def head_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.head))
		elif self.markup == 'textile': return mark_safe(textile(self.head))
		else: return mark_safe(self.head)

	def body_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.body))
		elif self.markup == 'textile': return mark_safe(textile(self.body))
		else: return mark_safe(self.body)

	def comments_enabled(self):
		if self.close_comments_after is None:
			return True
		else:
			return self.published + timedelta(self.close_comments_after) > timezone.now()

	class Meta:
		get_latest_by = 'published'
		ordering = ('-published',)
		verbose_name = _('article')
		verbose_name_plural = _('articles')


class Comment(models.Model):
	subject = models.CharField(_('subject'),max_length=100)
	article = models.ForeignKey(Article,verbose_name=_('article'))
	reply = models.ForeignKey('self',verbose_name=_('reply to'),null=True,blank=True)
	message = models.TextField(_('content'))
	sender = models.CharField(_('sender'),max_length=100)
	posted = models.DateTimeField(_('posted'),auto_now_add=True)
	ip = models.GenericIPAddressField(_('IP address'),blank=True,null=True)
	useragent = models.CharField(_('user agent'),max_length=100,blank=True)

	def get_absolute_url(self):
		return '%snews/%s/' % (self.article.get_absolute_url(),self.id)

	def path(self):
		return self.get_absolute_url()

	path.short_description = _("path")

	def level(self):
		if reply:
			return self.reply.level
		return 0

	def __unicode__(self):
		return u'%s -- %s (%s)' % (self.article,self.subject,self.posted.strftime('%Y-%m-%d %H:%M'))

	def get_absolute_url(self):
		return self.article.get_absolute_url()

	class Meta:
		get_latest_by = 'posted'
		ordering = ('-posted',)
		verbose_name = _('comment')
		verbose_name_plural = _('comments')

