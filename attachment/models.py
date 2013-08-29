# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Peter Kuma

import os

from django.utils.translation import ugettext_lazy as _
from django.db.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

class Attachment(Model):
	content_type = ForeignKey(ContentType, verbose_name=_('content type'))
	object_id = PositiveIntegerField(_('object ID'))
	content_object = GenericForeignKey('content_type', 'object_id')
	file = FileField(_('file'), upload_to=lambda i, f: 'attachment/%s/%s/%s/%s' %
			 (i.content_type.app_label, i.content_type.model, i.content_object.id, f))

	def __unicode__(self):
		if self.file:
			return unicode(os.path.basename(self.file.path))
		else:
			return u'Attachment object'

	def get_absolute_url(self):
		return self.file.url

	class Meta:
		verbose_name = _('attachment')
		verbose_name_plural = _('attachments')
