# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2012 Peter Kuma
# All rights reserved.
#

import os

from django.utils.translation import ugettext_lazy as _
from django.db.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

class Attachment(Model):
	content_type = ForeignKey(ContentType)
	object_id = PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	file = FileField(upload_to=lambda i, f: "attachment/%s/%s/%s/%s" %
			 (i.content_type.app_label, i.content_type.model, i.content_object.id, f))
	
	def __unicode__(self):
		return self.file.__unicode__()
	
	class Meta:
		verbose_name = _('attachment')
		verbose_name_plural = _('attachments')

