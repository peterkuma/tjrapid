# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

import csv

from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import *

@staff_member_required
def report(request, id, format, full=False):
	ev = get_object_or_404(Event, pk=id)
	participants = Participant.objects.filter(entry__event=ev)

	if format == 'csv':
		response = HttpResponse(mimetype='text/csv')
		response['Content-Disposition'] = 'attachment; filename=%s.csv' % ev
		writer = csv.writer(response)
		if full:
			writer.writerow([
				_('ID').encode('utf-8'),
				_('First name').encode('utf-8'),
				_('Surname').encode('utf-8'),
				_('Class').encode('utf-8'),
				_('Club').encode('utf-8'),
				_('SI').encode('utf-8'),
				_('SI mode').encode('utf-8'),
				_('Note').encode('utf-8'),
				_('Accommodation').encode('utf-8'),
				_('Accommodation count').encode('utf-8'),
				_('Accommodation nights').encode('utf-8'),
				_('Accommodation note').encode('utf-8'),
				_('Entry fee').encode('utf-8'),
				_('Accommodation fee').encode('utf-8'),
				_('SI fee').encode('utf-8'),
				_('Fees').encode('utf-8'),
			])
			for pa in participants:
				if pa.accomm != None:
					accommlabel = pa.accomm.label
				else:
					accommlabel = None
				list = [
					pa.id,
					pa.firstname,
					pa.surname,
					pa.cls,
					pa.club,
					pa.si,
					pa.simode,
					pa.note,
					accommlabel,
					pa.accommcount,
					pa.accommnights,
					pa.accommnote,
					pa.entryfee,
					pa.accommfee,
					pa.sifee,
					pa.fees(),
				]
				row = []
				for item in list:
					if item == None:
						row += ('',)
					else:
						row += (unicode(item).encode('utf-8'),)
				writer.writerow(row)
		return response
	raise Exception('Unknown format')
