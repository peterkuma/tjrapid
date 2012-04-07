# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.generic import GenericRelation

from attachment.models import Attachment
from main.models import *

class Article(models.Model):
	title = models.CharField(_('title'),max_length=100)
	category = models.ForeignKey(Category,verbose_name=_('category'))
	head = models.TextField(_('head'),blank=True,help_text=_('Text formatted in <a href="http://en.wikipedia.org/wiki/Textile_(markup_language)">Textile</a>. Attachments can be referenced in links and images by their file name. HTML is allowed.'))
	body = models.TextField(_('body'),blank=True,help_text=_('Text formatted in <a href="http://en.wikipedia.org/wiki/Textile_(markup_language)">Textile</a>. Attachments can be referenced in links and images by their file name. HTML is allowed.'))
	author = models.CharField(_('author'),max_length=100)
	published = models.DateTimeField(_('published'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)
	attachments = GenericRelation(Attachment)

	def get_absolute_url(self):
		return '%snews/article/%s/' % (self.category.get_absolute_url(), self.id)

	def path(self):
		return self.get_absolute_url()

	path.short_description = _("path")

	def __unicode__(self):
		return u'%s -- %s' % (self.category,self.title)

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

