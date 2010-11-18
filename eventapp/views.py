# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

import os
from datetime import datetime
from decimal import Decimal
import re
from smtplib import SMTPException
import socket
import logging
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import unicodedata

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import translation
from django import forms
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.core.exceptions import *
from django.template import Context, loader
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site

import urls
from models import *

def http500(request, error):
	t = loader.get_template('eventapp/500.html')
	c = RequestContext(request, {'error': error})
	return HttpResponseServerError(t.render(c))

class NewEntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('email', )
	
class ExistingEntryForm(forms.Form):
	id = forms.CharField(label=_('Entry identification code'), max_length=11)	
		
	def clean_id(self):
		data = self.cleaned_data['id']
		try:
			Entry.objects.get(pk=data)
		except Entry.DoesNotExist:
			raise ValidationError(_('Entry %s does not exist.') % data)
		return data

def event(request, id, namespace=None, **kwargs):
	class RecoveryForm(forms.Form):
		email = forms.EmailField()
		
		def clean_email(self):
			data = self.cleaned_data['email']
			try:
				er = Entry.objects.get(event=ev, email=data)
			except Entry.DoesNotExist:
				raise ValidationError(_('No matching entry found.'))
			return data
		
	ev = get_object_or_404(Event, pk=id)

	#if ev.close_date < datetime.date.today():
	#	return http500(request, _('The event was closed on %s.' % ev.close_date))
	if ev.open_date > datetime.date.today():
		return http500(request,  _('The event will open on %s.' % ev.open_date))

	if request.method == 'POST' and request.POST.has_key('newentry'):
		newentry_form = NewEntryForm(request.POST)
		if newentry_form.is_valid():
			er = newentry_form.save(commit=False)
			er.event = ev
			t = loader.get_template('eventapp/newentry-email.txt')
			c = Context({
				'id': er.id,
				'event_title': ev.title,
				'event_url': reverse('eventapp:event', kwargs=dict(id=ev.id), current_app=namespace),
				'entry_url': reverse('eventapp:entry', kwargs=dict(eventid=ev.id, id=er.id), current_app=namespace),
				'domain': Site.objects.get_current().domain,
			})
			try:
				send_mail(unicodedata.normalize('NFKD', _('New entry information')).encode('ascii', 'ignore'),
					  unicodedata.normalize('NFKD', t.render(c)).encode('ascii', 'ignore'),
					  unicodedata.normalize('NFKD', _('Event organiser <%s>') % ev.email).encode('ascii', 'ignore'),
					  (er.email,))
			except (socket.error, SMTPException), e:
				if (settings.DEBUG):
					raise e
				log = logging.getLogger('django')
				log.error('Failed to send mail: %s', e)
				return http500(request, _('Failed to send mail.'))
			
			er.save(force_insert=True)
			return HttpResponseRedirect(reverse('eventapp:new-participant', kwargs=dict(eventid=ev.id, entryid=er.id), current_app=namespace))
	else:
		newentry_form = NewEntryForm()
	
	if request.method == 'POST' and request.POST.has_key('existingentry'):
		existingentry_form = ExistingEntryForm(request.POST)
		if existingentry_form.is_valid():
			return HttpResponseRedirect(reverse('eventapp:entry', kwargs=dict(
				eventid=ev.id,
				id=existingentry_form.cleaned_data['id']), current_app=namespace))
	else:
		existingentry_form = ExistingEntryForm()
	
	if request.method == 'POST' and request.POST.has_key('recovery'):
		recovery_form = RecoveryForm(request.POST)
		if recovery_form.is_valid():
			er = Entry.objects.get(event=ev, email=recovery_form.cleaned_data['email'])
			t = loader.get_template('eventapp/recovery-email.txt')
			c = Context({
				'id': er.id,
				'event_title': ev.title,
				'event_url': reverse('eventapp:event', kwargs=dict(id=ev.id), current_app=namespace),
				'entry_url': reverse('eventapp:entry', kwargs=dict(eventid=ev.id, id=er.id), current_app=namespace),
				'domain': Site.objects.get_current().domain,
			})
			try:
				send_mail(unicodedata.normalize('NFKD', _('Entry identification code recovery')).encode('ascii', 'ignore'),
					  unicodedata.normalize('NFKD', t.render(c)).encode('ascii', 'ignore'),
					  unicodedata.normalize('NFKD', _('Event organiser <%s>') % ev.email).encode('ascii', 'ignore'),
					  (er.email,))
			except (socket.error, SMTPException), e:
				if (settings.DEBUG):
					raise e
				log = logging.getLogger('django')
				log.error('Failed to send mail: %s', e)
				return http500(request, _('Failed to send mail.'))
	
			return render_to_response('eventapp/recovery_response.html', {
					'event': ev,
					'email': recovery_form.cleaned_data['email'],
				}, RequestContext(request))
	else:
		recovery_form = RecoveryForm()
	
	return render_to_response('eventapp/event.html', {
			'event': ev, 
			'newentry_form': newentry_form, 
			'existingentry_form': existingentry_form,
			'recovery_form': recovery_form,
		},
		RequestContext(request)
	)

def entry(request, eventid, id, **kwargs):
	ev = get_object_or_404(Event, pk=eventid)
	er = get_object_or_404(Entry, pk=id, event=ev)
	
	#if ev.close_date < datetime.date.today():
	#	return http500(request, _('The event was closed on %s' % ev.close_date))
	#elif ev.open_date > datetime.date.today():
	#	return http500(request,  _('The event will open on %s' % ev.open_date))
	
	participants = Participant.objects.filter(entry=er)
	total = Decimal(0)
	for pa in participants:
		total += pa.fees()
	
	return render_to_response('eventapp/entry.html',  {
			'event': ev, 
			'entry': er, 
			'participants': participants, 
			'total': total,
		}, 
		RequestContext(request)
	)

def participant(request, eventid,  entryid,  id=None, namespace=None, **kwargs):
	ev = get_object_or_404(Event,  pk=eventid)
	er = get_object_or_404(Entry,  pk=entryid,  event=ev)

	if ev.close_date < datetime.date.today():
		return http500(request, _('The event was closed on %s.' % ev.close_date))
	elif ev.open_date > datetime.date.today():
		return http500(request,  _('The event will open on %s.' % ev.open_date))
		
	if id != None:
		pa = get_object_or_404(Participant,  pk=id)
	else:
		pa = None
	
	if request.POST.has_key('remove'):
		pa.delete()
		return HttpResponseRedirect(reverse('eventapp:entry', kwargs=dict(eventid=ev.id, id=er.id), current_app=namespace))
	
	classfees = ClassFee.objects.filter(
		Q(start_date=None) | Q(start_date__lte=datetime.datetime.now()),
		Q(end_date=None) | Q(end_date__gte=datetime.datetime.now()), 
		event=ev
	)
	
	clsdict = {}
	for classfee in classfees:
		classes = re.split(r'\s*,\s*', classfee.classes)
		for c in classes:
			clsdict[c] = classfee.fee
	if pa != None:
		clsdict[pa.cls] = pa.entryfee
	keys = clsdict.keys()
	keys.sort()
	clschoices = [(k, u'%s (%s €)' % (k,  clsdict[k])) for k in keys]
	
	class ParticipantForm(forms.ModelForm):
		cls = forms.ChoiceField(choices=clschoices,
			label=Participant._meta.get_field('cls').verbose_name.capitalize(),
			help_text=Participant._meta.get_field('cls').help_text
		)
		
		class Meta:
			model = Participant
			exclude = ('id', 'entry', 'cls', 'accommfee', 'entryfee', 'sifee')
						
		def clean(self):
			si = self.cleaned_data.get('si')
			simode = self.cleaned_data.get('simode')
			if simode == 'P' and si == None:
				self._errors['si'] = self.error_class([_('The SI number is invalid.')])
			
			accomm = self.cleaned_data.get('accomm')
			accommcount = self.cleaned_data.get('accommcount')
			accommnights = self.cleaned_data.get('accommnights')
			if accomm != None and accommcount != None:
				if pa != None and accomm == pa.accomm and accomm.free() + pa.accommcount < accommcount or pa == None and accomm.free() < accommcount:
					self._errors['accomm'] = self.error_class([_('There are not as many places available in the accommodation selected.')])
					del self.cleaned_data['accomm']
					
			return self.cleaned_data
	
	if request.method == 'POST' and request.POST.has_key('commit'):
		form = ParticipantForm(request.POST, instance=pa)
		simode = form.data['simode']
		if form.is_valid():
			pa = form.save(commit=False)
			if pa.simode != 'P':
				pa.si = None
			pa.cls = form.cleaned_data['cls']
			pa.entry = er
			pa.entryfee = clsdict[form.cleaned_data['cls']]
			if ev.sifee != None and pa.simode == 'B':
				pa.sifee = ev.sifee
			else:
				pa.sifee = 0
			if pa.accomm != None:
				pa.accommfee = pa.accomm.price * pa.accommcount * pa.accommnights
			pa.save(force_insert=(id == None))
			
			return HttpResponseRedirect(reverse('eventapp:entry', kwargs=dict(eventid=ev.id, id=er.id), current_app=namespace))
	elif id != None:
		form = ParticipantForm(instance=pa, initial={'cls': pa.cls })
		simode = pa.simode
	else:
		form = ParticipantForm()
		simode = form.fields['simode'].initial
		
	form.fields['accomm'].queryset = Accommodation.objects.filter(event=ev)
	del form.fields['accommnights'].choices[0]
	del form.fields['accommcount'].choices[0]

	return render_to_response('eventapp/participant.html',  {
			'event': ev, 
			'entry': er, 
			'participant': pa, 
			'form': form, 
			'simode': simode, 
			'accommodation': Accommodation.objects.filter(event=ev),
		}, 
		RequestContext(request)
	)


def entry_pdf(request, eventid, id, **kwargs):	
	pdfmetrics.registerFont(TTFont('regular', settings.RGFONT))
	pdfmetrics.registerFont(TTFont('bold', settings.BDFONT))
	pdfmetrics.registerFont(TTFont('italic', settings.ITFONT))
	
	font = 'regular'
	bdfont = 'bold'
	itfont = 'italic'
	
	ev = get_object_or_404(Event, pk=eventid)
	er = get_object_or_404(Entry, pk=id, event=ev)
	
	participants = Participant.objects.filter(entry=er)
	total = Decimal(0)
	for pa in participants:
		total += pa.fees()
	
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
	
	issue_datetime = datetime.datetime.now()
	
	def print_headline(page, num_pages):
		c.translate(3*cm, -4.5*cm)
		c.saveState()
		c.setFont(font, 24)
		c.drawString(0, 0, _('Entry Statement'))
		c.setFont(font, 14)
		c.drawRightString(width-5*cm, 0, _('Page %(page)d of %(num_pages)d') % dict(page=page, num_pages=num_pages))
		c.restoreState()
		c.translate(0, -2*cm)
	
		c.drawString(0, 0, _('Event: %s') % ev)
		c.translate(0, -8*mm)
		c.drawString(0, 0, _('Issue time: %s') % issue_datetime.strftime('%Y-%m-%d %H:%M %Z'))
		c.translate(0, -8*mm)
		
		c.translate(0, -1*cm)
	
	def print_participant(pa, n):
		c.drawString(0, 0, '%d.' % n)
		c.saveState()
		c.setFont(bdfont, 12)
		c.drawString(1*cm, 0, u'%s %s' % (pa.firstname, pa.surname))
		c.restoreState()
		c.translate(0, -8*mm)

		c.saveState()
		c.drawString(0, 0, _('Registration:'))
		c.setFont(itfont, 12)
		c.drawString(4*cm, 0, u'%s, %s (%s €)' % (pa.club, pa.cls, pa.entryfee))
		c.restoreState()
		c.translate(0, -8*mm)

		c.saveState()
		c.drawString(0, 0, _(u'SI token:'))
		c.setFont(itfont, 12)
		if pa.sifee > 0:
			c.drawString(4*cm, 0, u'%s (%s €)' % (pa.get_si_display(), pa.sifee))
		else:
			c.drawString(4*cm, 0, u'%s' % pa.get_si_display())
		c.restoreState()
		c.translate(0, -8*mm)

		if pa.accomm:
			c.saveState()
			c.drawString(0, 0, _('Accommodation:'))
			c.setFont(itfont, 12)
			c.drawString(4*cm, 0, u'%s, %s, %s (%s €)' % (pa.accomm.label, pa.get_accommcount_display(), pa.get_accommnights_display(), pa.accommfee))
			c.restoreState()
			c.translate(0, -8*mm)
			
		c.saveState()
		c.setFont(font, 14)
		c.drawRightString(width-5*cm, 7*mm, u'%s €' % pa.fees())
		c.restoreState()
		
		c.translate(0, -4*mm)
	
	mm = 2.835
	cm = 10*mm
	width = 210*mm
	height = 297*mm
	c = canvas.Canvas(response, pagesize=(width, height))
	c.translate(0, height)
	c.setFont(font, 12)
	
	if len(participants) == 0:
		print_headline(1, 1)
		c.drawString(0, 0, _('No participants in this entry.'))
	else:
		i = 0
		participants_per_page = 5
		for pa in participants:
			if i % participants_per_page == 0:
				if i != 0:
					c.showPage()
					c.translate(0, height)
				print_headline(i/participants_per_page + 1,
					       (len(participants)-1)/participants_per_page + 1)
			print_participant(pa, i+1)	
			i = i + 1	
		c.translate(0, -1*cm)
		c.setFont(font, 16)
		c.drawString(0, 0, _('Total:'))
		c.drawRightString(width-5*cm, 0, u'%s €' % total)	

	c.showPage()
	c.save()
	return response
