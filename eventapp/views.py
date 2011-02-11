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
from django.core import serializers

import urls
from models import *

def http500(request, error):
	t = loader.get_template('eventapp/500.html')
	c = RequestContext(request, {'error': error})
	return HttpResponseServerError(t.render(c))

def event(request, id, namespace=None, **kwargs):
	ev = get_object_or_404(Event, pk=id)

	class NewEntryForm(forms.ModelForm):
		class Meta:
			model = Entry
			fields = ('event', 'email', )
			
		def clean_email(self):
			email = self.cleaned_data['email']
			if Entry.objects.filter(event=ev, email=email).exists():
				raise ValidationError(_('An entry with this e-mail already exists. Please use the link from the message you have received, or use the form below to recover your entry identification code.'))
			return email
		
	class ExistingEntryForm(forms.Form):
		id = forms.CharField(label=_('Entry identification code'), max_length=11)	
			
		def clean_id(self):
			data = self.cleaned_data['id']
			try:
				Entry.objects.get(pk=data)
			except Entry.DoesNotExist:
				raise ValidationError(_('Entry %s does not exist.') % data)
			return data

	class RecoveryForm(forms.Form):
		email = forms.EmailField()
		
		def clean_email(self):
			data = self.cleaned_data['email']
			try:
				er = Entry.objects.get(event=ev, email=data)
			except Entry.DoesNotExist:
				raise ValidationError(_('No matching entry found.'))
			return data
	
	#if ev.close_date < datetime.date.today():
	#	return http500(request, _('The event was closed on %s.' % ev.close_date))
	if ev.open_date > datetime.date.today():
		return http500(request,  _('The event will open on %s.' % ev.open_date))

	if request.method == 'POST' and request.POST.has_key('newentry'):
		newentry_form = NewEntryForm(dict(event=id, email=request.POST['email']))
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

def action(request, eventid,  entryid, namespace=None, **kwargs):
	ev = get_object_or_404(Event,  pk=eventid)
	er = get_object_or_404(Entry,  pk=entryid,  event=ev)

	if ev.close_date < datetime.date.today():
		return http500(request, _('The event was closed on %s.' % ev.close_date))
	elif ev.open_date > datetime.date.today():
		return http500(request,  _('The event will open on %s.' % ev.open_date))
		
	action = request.POST.get('action')
	selected = request.POST.getlist('selected')
	
	participants = Participant.objects.filter(entry=er)
	for pa in participants:
		if pa.id in selected:
			if action == "remove":
				pa.delete()
		
	return HttpResponseRedirect(reverse('eventapp:entry', kwargs=dict(eventid=ev.id, id=er.id), current_app=namespace))

def list(request, eventid,  entryid, namespace=None, **kwargs):
	ev = get_object_or_404(Event,  pk=eventid)
	er = get_object_or_404(Entry,  pk=entryid,  event=ev)

	participants = Participant.objects.filter(entry__event=ev)

	return render_to_response('eventapp/list.html',  {
			'event': ev, 
			'entry': er, 
			'participants': participants, 
		}, RequestContext(request)
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
			c = c[0:10]
			clsdict[c] = (classfee.fee, classfee.lapfee, classfee.lapsifee)
	#if pa != None:
	#	clsdict[pa.cls] = pa.entryfee
	keys = clsdict.keys()
	keys.sort()
	clschoices = []
	for k in keys:
		if clsdict[k][1] != None and clsdict[k][0] != clsdict[k][1]:
			clschoices.append((k, _(u'%(cls)s (%(fee)s € or %(lapfee)s € per lap)') % dict(cls=k, fee=clsdict[k][0], lapfee=clsdict[k][1])))
		else:
			clschoices.append((k, _(u'%(cls)s (%(fee)s €)') % dict(cls=k,  fee=clsdict[k][0])))
	
	class ParticipantForm(forms.ModelForm):
		cls = forms.ChoiceField(choices=clschoices,
			label=Participant._meta.get_field('cls').verbose_name.capitalize(),
			help_text=Participant._meta.get_field('cls').help_text
		)
		laps = forms.MultipleChoiceField(choices=zip(range(1,ev.laps+1),range(1,ev.laps+1)),
			label=Participant._meta.get_field('laps').verbose_name.capitalize(),
			widget=forms.CheckboxSelectMultiple(),
			initial=range(1,ev.laps+1),
		)
		
		class Meta:
			model = Participant
			exclude = ('id', 'entry', 'cls', 'accommfee', 'entryfee', 'sifee')
		
		def clean_laps(self):
			laps_raw = self.cleaned_data['laps']
			return ','.join(laps_raw)
					
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
			clsfee = clsdict[form.cleaned_data['cls']]
			if pa.laps_count() != ev.laps and clsfee[1] != None:
				pa.entryfee = clsfee[1] * pa.laps_count()
			else:
				pa.entryfee = clsfee[0]
			if pa.simode == 'B':
				if pa.laps_count() != ev.laps and clsfee[2] != None:
					pa.sifee = clsfee[2] * pa.laps_count()
				elif ev.sifee != None:
					pa.sifee = ev.sifee
			else:
				pa.sifee = 0
			if pa.accomm != None and pa.accommcount != None and pa.accommnights != None:
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
	ev = get_object_or_404(Event, pk=eventid)
	er = get_object_or_404(Entry, pk=id, event=ev)
	participants = Participant.objects.filter(entry=er)
	issue_datetime = datetime.datetime.now()
	
	from reportlab.pdfbase import pdfmetrics
	from reportlab.pdfbase.ttfonts import TTFont
	from reportlab.lib.pagesizes import A4
	from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
	from reportlab.lib.styles import ParagraphStyle
	from reportlab.lib import colors
	from reportlab.lib.units import inch, cm
	
	# Set up fonts.
	pdfmetrics.registerFont(TTFont('regular', settings.RGFONT))
	pdfmetrics.registerFont(TTFont('bold', settings.BDFONT))
	pdfmetrics.registerFont(TTFont('italic', settings.ITFONT))
	
	font = 'regular'
	bdfont = 'bold'
	itfont = 'italic'
	
	# Declare styles.
	normal = ParagraphStyle('normal',
				 fontName=font,
				 fontSize=10,
				 spaceBefore=0.5*cm,
				 spaceAfter=0.5*cm,
	)
	heading1 = ParagraphStyle('heading1',
				 fontName=bdfont,
				 fontSize=18,
				 spaceBefore=0.6*cm,
				 spaceAfter=1.5*cm,
	)
	heading2 = ParagraphStyle('heading2',
				 fontName=itfont,
				 fontSize=14,
				 spaceBefore=0.5*cm,
				 spaceAfter=0.8*cm,
	)
	
	def truncate(s, n):
		return u'%s…' % s[0:n-2] if len(s) > n else s
	
	def participants_table():
		data = []
		data.append(['#', _('Name'), _('Club'), _('Class'), _('Laps'), _('SI'), _('Accomm.'), _('Entry/SI/Accomm. fee'), _('Fees')])
		i = 1
		for pa in participants:			
			data.append([
				i,
				truncate(pa.firstname + ' ' + pa.surname, 25),
				pa.club,
				pa.cls,
				pa.laps,
				unicode(pa.get_si_abbr()),
				truncate(pa.accomm.label, 20) if pa.accomm else '',
				u'%s/%s/%s €' % (pa.entryfee, pa.sifee, pa.accommfee),
				u'%s €' % pa.fees(),
			])
			i = i + 1
		extrafees = u'%s/%s/%s €' % (er.entryfees(), er.sifees(), er.accommfees())
		data.append([_('Total'),'','','','','','',extrafees,u'%s €' % er.fees()])
		
		last = len(data) - 1
		tstyle = TableStyle()
		tstyle.add('FONT', (0,0), (-1,0), bdfont, 8)
		tstyle.add('FONT', (0,1), (-1,-1), font, 8)
		tstyle.add('LINEABOVE', (0,0), (-1,0), 1, colors.black)
		tstyle.add('LINEBELOW', (0,0), (-1,0), 1, colors.black)
		tstyle.add('FONT', (0,-1), (-1,-1), bdfont, 8)
		tstyle.add('LINEABOVE', (0,-1), (-1,-1), 1, colors.black)
		tstyle.add('LINEBELOW', (0,-1), (-1,-1), 1, colors.black)
		tstyle.add('ALIGN', (-2,0), (-1,-1), 'RIGHT')
		tstyle.add('SPAN', (0,last), (-3,last))
		t = Table(data)
		t.setStyle(tstyle)
		return t
	
	def firstpage(c, doc):
		c.saveState()
		c.setFont(bdfont, 10)
		c.drawRightString(A4[0]-1.5*cm, 2*cm, unicode(doc.page))
		c.restoreState()
	
	def nextpage(c, doc):
		c.saveState()
		c.setFont(itfont, 10)
		c.drawString(1.5*cm, A4[1]-2*cm, unicode(ev))
		c.setFont(font, 10)
		c.drawCentredString(A4[0]/2, A4[1]-2*cm, _('Entry Statement'))
		c.setFont(bdfont, 10)
		c.drawRightString(A4[0]-1.5*cm, A4[1]-2*cm, unicode(doc.page))
		c.setLineWidth(0.5)
		c.line(1.4*cm, A4[1]-2.2*cm, A4[0]-1.4*cm, A4[1]-2.2*cm)
		c.restoreState()
	
	story = []
	story.append(Paragraph(unicode(ev), heading2))
	story.append(Paragraph(_('Entry Statement'), heading1))
	from django.utils import formats
	story.append(Paragraph(formats.date_format(issue_datetime, 'DATETIME_FORMAT'), normal))
	story.append(Spacer(0.5*cm, 0.5*cm))
	if participants:
		story.append(participants_table())
	else:
		story.append(Paragraph(_('There are no participants in this entry.'), normal))

	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=%s' % _('entry-statement.pdf')
	doc = SimpleDocTemplate(response,
				pagesize=A4,
				title=_('Entry Statement'),
				leftMargin=1.5*cm,
				rightMargin=1.5*cm,
				topMargin=2.5*cm,
				bottomMargin=3*cm)
	doc.build(story, onFirstPage=firstpage, onLaterPages=nextpage)	
	return response


def query(request, eventid,  entryid,  id=None, namespace=None, **kwargs):
	ev = get_object_or_404(Event,  pk=eventid)
	er = get_object_or_404(Entry,  pk=entryid,  event=ev)

	if id != None:
		pa = get_object_or_404(Participant,  pk=id)
	else:
		pa = None
	
	q = request.GET.get("q", None)
	
	if q == None or len(q) == 0:
		people = []
	else:
		people = Directory.objects.filter(surname__istartswith=q)
		
	response = HttpResponse()
	json_serializer = serializers.get_serializer("json")()
	json_serializer.serialize(people, ensure_ascii=False, stream=response,
				  fields=('firstname', 'surname', 'club', 'si', 'cls'))
	return response
