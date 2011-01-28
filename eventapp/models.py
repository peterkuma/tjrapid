# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from os import urandom

ACCOMMNIGHTS_CHOICES = (
	(1,  _('1 night')), 
	(2,  _('2 nights')), 
	(3,  _('3 nights')), 
	(4,  _('4 nights')), 
	(5,  _('5 nights')), 
	(6,  _('6 nights')), 
	(7,  _('7 nights')), 
	(8,  _('8 nights')), 
	(9,  _('9 nights')), 
	(10,  _('10 nights')), 
)

ACCOMMCOUNT_CHOICES = (
	(1,  _('1 person')), 
	(2,  _('2 people')),
	(3,  _('3 people')),
	(4,  _('4 people')),
	(5,  _('5 people')),
	(6,  _('6 people')),
)

SIMODE_CHOICES = (
	('L', _('later')),
	('B', _('borrow')),
	('P', _('present')),
)

def genid(what):
	return '%s%02d%02d-%02d%02d' % (what, 
		ord(urandom(1)) % 100, ord(urandom(1)) % 100,
		ord(urandom(1)) % 100, ord(urandom(1)) % 100)

class Event(Model):
	id = CharField(_('ID'), primary_key=True, default=lambda: genid('EV'), max_length=11)
	title = CharField(_('title'), max_length=50)
	sifee = DecimalField(_('si fee'), max_digits=10, decimal_places=2, blank=True, null=True)
	open_date = DateField(_('open date'), default=datetime.datetime.now)
	close_date = DateField(_('close date'))
	email = EmailField(_('e-mail'))
	laps = PositiveIntegerField(_('number of laps'), default=1)
	
	def is_open(self):
		return self.open_date <= datetime.date.today() and self.close_date >= datetime.date.today()
	
	def __unicode__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('eventapp:event', (), dict(id=self.id))

	class Meta:
		verbose_name = _('event')
		verbose_name_plural = _('events')
		ordering = ('open_date', )

class ClassFee(Model):
	event = ForeignKey('Event', db_column='eventid', verbose_name=_('event'))
	label = CharField(_('label'), max_length=50)
	classes = TextField(_('classes'))
	start_date = DateField(_('start date'), blank=True, null=True)
	end_date = DateField(_('end_date'), blank=True, null=True)
	fee = DecimalField(_('fee'), max_digits=10, decimal_places=2)
	lapfee = DecimalField(_('lap fee'), max_digits=10, decimal_places=2, blank=True, null=True)

	def __unicode__(self):
		return self.label

	class Meta:
		verbose_name = _('class fee')
		verbose_name_plural = _('class fees')
		unique_together = (('event', 'label'),)
		ordering = ('event', 'label')

class Entry(Model):
	id = CharField(_('ID'), primary_key=True, default=lambda: genid('ER'), max_length=11)
	event = ForeignKey('Event', db_column='eventid', verbose_name=_('event'))
	email = EmailField(_('e-mail'))
	created = DateTimeField(_('created'),auto_now_add=True)
	modified = DateTimeField(_('modified'),auto_now=True)
	
	def __unicode__(self):
		return self.id

	@permalink
	def get_absolute_url(self):
		return ('eventapp:entry', (), dict(eventid=self.event.id, id=self.id))	

	def entryfees(self):
		return Participant.objects.filter(entry=self).aggregate(Sum('entryfee'))['entryfee__sum']
		
	def sifees(self):
		return Participant.objects.filter(entry=self).aggregate(Sum('sifee'))['sifee__sum']
	
	def accommfees(self):
		return Participant.objects.filter(entry=self).aggregate(Sum('accommfee'))['accommfee__sum']

	def fees(self):
		return self.entryfees() + self.sifees() + self.accommfees()

	class Meta:
		verbose_name = _('entry')
		verbose_name_plural = _('entries')
		ordering = ('event', 'created')
		unique_together = (('event', 'email'),)

	
class Accommodation(Model):
	id = CharField(_('ID'), primary_key=True, default=lambda: genid('AC'), max_length=11)
	event = ForeignKey('Event',  db_column='eventid', verbose_name=_('event'))
	label = CharField(_('label'), max_length=50)
	price = DecimalField(_('price'), max_digits=10, decimal_places=2, help_text='Price per night')
	minnights = PositiveSmallIntegerField(_('minimum nights'), default=1)
	maxnights = PositiveSmallIntegerField(_('maximum nights'))
	capacity = PositiveSmallIntegerField(_('capacity'),  blank=True,  null=True)
	
	def __unicode__(self):
		return _(u'%(label)s (%(price)s € per night)') % dict(label=self.label,  price=self.price)

	def free(self):
		if self.capacity == None:
			return 32767
		free = self.capacity
		for pa in self.participant_set.all():
			if (pa.accommcount != None):
				free -= pa.accommcount
		if free < 0:
			return 0
		else:
			return free

	class Meta:
		verbose_name = _('accommodation')
		verbose_name_plural = _('accommodation')
		unique_together = (('event', 'label'),)
		ordering = ('event', 'label')
	
class Participant(Model):
	id = CharField(_('ID'), primary_key=True, default=lambda: genid('PA'), max_length=11)
	entry = ForeignKey('Entry',  db_column='entryid', verbose_name=_('entry'))
	firstname = CharField(_('first name'), max_length=50)
	surname = CharField(_('surname'), max_length=50)
	club = CharField(_('club'), max_length=7,  help_text=_('Club and membership number, e.g. RBA1234. If registering as an individual, enter XXXyy, where yy is the year of birth, e.g. XXX80.'))
	si = DecimalField(_('SI'), max_digits=9, decimal_places=0, blank=True, null=True)
	simode = CharField(_('SI mode'),  max_length=1,  choices=SIMODE_CHOICES, default='P')
	cls = CharField(_('class'), max_length=10)
	laps = CommaSeparatedIntegerField(_('laps'), max_length=50,)
	note = TextField(_('note'), blank=True)
	accomm = ForeignKey('Accommodation', db_column='accomid', verbose_name=_('accommodation'), blank=True,  null=True)
	accommcount = PositiveSmallIntegerField(_('accommodation count'),  default=1, blank=True, null=True, choices=ACCOMMCOUNT_CHOICES)
	accommnights = PositiveSmallIntegerField(_('accommodation nights'), default=1, blank=True, null=True, choices=ACCOMMNIGHTS_CHOICES)
	accommnote = TextField(_('accommodation note'), blank=True)
	accommfee = DecimalField(_('accommodation fee'), max_digits=10, decimal_places=2, default=0)
	entryfee = DecimalField(_('entry fee'), max_digits=10, decimal_places=2, default=0)
	sifee = DecimalField(_('SI fee'), max_digits=10, decimal_places=2, default=0)
	created = DateTimeField(_('created'),auto_now_add=True)
	modified = DateTimeField(_('modified'),auto_now=True)

	def __unicode__(self):
		return self.id

	def fees(self):
		return self.entryfee + self.accommfee + self.sifee

	def laps_list(self):
		return [int(l) for l in self.laps.split(',')]

	def laps_count(self):
		return len(self.laps_list())

	def get_si_display(self):
		if self.simode == 'L':
			return _('supply later')
		elif self.simode == 'B':
			return _('want to borrow')
		else:
			return self.si

	def get_si_abbr(self):
		if self.simode == 'L':
			return _('later')
		elif self.simode == 'B':
			return _('borrow')
		else:
			return self.si
	
	def save(self, *args, **kwargs):
		Model.save(self, *args, **kwargs)
		self.entry.modified = datetime.datetime.now()
		self.entry.save()

	class Meta:
		verbose_name = _('participant')
		verbose_name_plural = _('participants')
		ordering = ('club', 'surname', 'firstname')

class Directory(Model):
	firstname = CharField(_('first name'), max_length=50)
	surname = CharField(_('surname'), max_length=50)
	club = CharField(_('club'), max_length=7, null=True)
	si = DecimalField(_('SI'), max_digits=9, decimal_places=0, blank=True, null=True)
	cls = CharField(_('class'), max_length=10, null=True)
	created = DateTimeField(_('created'),auto_now_add=True)
	modified = DateTimeField(_('modified'),auto_now=True)

	def __unicode__(self):
		return self.firstname + " " + self.surname
	
	class Meta:
		verbose_name = _('directory')
		verbose_name_plural = _('directory')
		ordering = ('surname', 'firstname')

