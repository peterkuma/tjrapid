# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Peter Kuma

import os
from datetime import date, datetime
import urllib.request, urllib.error, urllib.parse
import json
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from markdown import markdown
from textile import textile
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.fields import GenericRelation
from django_attach.models import Attachment
from linguo.models import MultilingualModel
from linguo.managers import MultilingualManager
from django.urls import reverse
from django.utils.translation import get_language
from django.core.validators import MaxValueValidator

from main.models import Category


MARKUP_CHOICES = (
	('markdown', 'Markdown'),
	('textile', 'Textile'),
	('html', 'HTML'),
)


MARKERS = (
	'amenity/arts_centre',
	'amenity/atm',
	'amenity/bank',
	'amenity/bar',
	'amenity/bbq',
	'amenity/bench',
	'amenity/bicycle_parking',
	'amenity/bicycle_repair_station',
	'amenity/biergarten',
	'amenity/boat_rental',
	'amenity/bureau_de_change',
	'amenity/bus_station',
	'amenity/cafe',
	'amenity/car_wash',
	'amenity/casino',
	'amenity/charging_station',
	'amenity/cinema',
	'amenity/community_centre',
	'amenity/courthouse',
	'amenity/dentist',
	'amenity/doctors',
	'amenity/drinking_water',
	'amenity/emergency_phone',
	'amenity/excrement_bags',
	'amenity/fast_food',
	'amenity/ferry',
	'amenity/firestation',
	'amenity/fountain',
	'amenity/fuel',
	'amenity/hospital',
	'amenity/hunting_stand',
	'amenity/ice_cream',
	'amenity/internet_cafe',
	'amenity/library',
	'amenity/motorcycle_parking',
	'amenity/nightclub',
	'amenity/parking',
	'amenity/parking_entrance_multistorey',
	'amenity/parking_entrance_underground',
	'amenity/parking_subtle',
	'amenity/parking_tickets',
	'amenity/pharmacy',
	'amenity/place_of_worship',
	'amenity/police',
	'amenity/post_box',
	'amenity/post_office',
	'amenity/prison',
	'amenity/pub',
	'amenity/public_bath',
	'amenity/public_bookcase',
	'amenity/public_transport_tickets',
	'amenity/recycling',
	'amenity/rental_bicycle',
	'amenity/rental_car',
	'amenity/restaurant',
	'amenity/shelter',
	'amenity/shower',
	'amenity/social_facility',
	'amenity/taxi',
	'amenity/telephone',
	'amenity/theatre',
	'amenity/toilets',
	'amenity/town_hall',
	'amenity/vehicle_inspection',
	'amenity/veterinary',
	'amenity/waste_basket',
	'amenity/waste_disposal',
	'barrier/cattle_grid',
	'barrier/cycle_barrier',
	'barrier/full-height_turnstile',
	'barrier/gate',
	'barrier/kissing_gate',
	'barrier/lift_gate',
	'barrier/motorcycle_barrier',
	'barrier/stile',
	'barrier/toll_booth',
	'highway/bus_stop',
	'highway/elevator',
	'highway/ford',
	'highway/traffic_light',
	'historic/archaeological_site',
	'historic/bust',
	'historic/castle',
	'historic/city_gate',
	'historic/fort',
	'historic/fortress',
	'historic/manor',
	'historic/memorial',
	'historic/monument',
	'historic/obelisk',
	'historic/palace',
	'historic/plaque',
	'historic/shrine',
	'historic/statue',
	'historic/stone',
	'leisure/amusement_arcade',
	'leisure/beach_resort',
	'leisure/bird_hide',
	'leisure/bowling_alley',
	'leisure/firepit',
	'leisure/fishing',
	'leisure/fitness',
	'leisure/golf',
	'leisure/miniature_golf',
	'leisure/outdoor_seating',
	'leisure/playground',
	'leisure/sauna',
	'leisure/slipway',
	'leisure/water_park',
	'man_made/bell_tower',
	'man_made/chimney',
	'man_made/communications_tower',
	'man_made/crane',
	'man_made/cross',
	'man_made/lighthouse',
	'man_made/mast',
	'man_made/mast_communications',
	'man_made/mast_lighting',
	'man_made/power_tower',
	'man_made/power_tower_small',
	'man_made/storage_tank',
	'man_made/telescope_dish',
	'man_made/telescope_dome',
	'man_made/tower_cantilever_communication',
	'man_made/tower_cooling',
	'man_made/tower_defensive',
	'man_made/tower_dish',
	'man_made/tower_dome',
	'man_made/tower_generic',
	'man_made/tower_lattice',
	'man_made/tower_lattice_communication',
	'man_made/tower_lattice_lighting',
	'man_made/tower_lighting',
	'man_made/tower_observation',
	'man_made/water_tower',
	'man_made/windmill',
	'natural/cave',
	'natural/peak',
	'natural/saddle',
	'office/consulate',
	'office/embassy',
	'religion/buddhist',
	'religion/christian',
	'religion/hinduist',
	'religion/jewish',
	'religion/muslim',
	'religion/shintoist',
	'religion/sikhist',
	'religion/taoist',
	'shop/alcohol',
	'shop/art',
	'shop/bag',
	'shop/bakery',
	'shop/beauty',
	'shop/bed',
	'shop/beverages',
	'shop/bicycle',
	'shop/bookmaker',
	'shop/butcher',
	'shop/car',
	'shop/car_parts',
	'shop/carpet',
	'shop/car_repair',
	'shop/charity',
	'shop/chemist',
	'shop/clothes',
	'shop/coffee',
	'shop/computer',
	'shop/confectionery',
	'shop/convenience',
	'shop/copyshop',
	'shop/dairy',
	'shop/deli',
	'shop/department_store',
	'shop/diy',
	'shop/electronics',
	'shop/fabric',
	'shop/florist',
	'shop/furniture',
	'shop/garden_centre',
	'shop/gift',
	'shop/greengrocer',
	'shop/hairdresser',
	'shop/hifi',
	'shop/houseware',
	'shop/interior_decoration',
	'shop/jewelry',
	'shop/laundry',
	'shop/marketplace',
	'shop/massage',
	'shop/medical_supply',
	'shop/mobile_phone',
	'shop/music',
	'shop/musical_instrument',
	'shop/newsagent',
	'shop/optician',
	'shop/outdoor',
	'shop/paint',
	'shop/perfumery',
	'shop/pet',
	'shop/photo',
	'shop/seafood',
	'shop/second_hand',
	'shop/shoes',
	'shop/sports',
	'shop/stationery',
	'shop/supermarket',
	'shop/tea',
	'shop/ticket',
	'shop/tobacco',
	'shop/toys',
	'shop/trade',
	'shop/travel_agency',
	'shop/tyres',
	'shop/variety_store',
	'shop/video',
	'shop/video_games',
	'tourism/alpinehut',
	'tourism/apartment',
	'tourism/artwork',
	'tourism/audioguide',
	'tourism/board',
	'tourism/camping',
	'tourism/caravan_park',
	'tourism/chalet',
	'tourism/guest_house',
	'tourism/guidepost',
	'tourism/hostel',
	'tourism/hotel',
	'tourism/information',
	'tourism/map',
	'tourism/motel',
	'tourism/museum',
	'tourism/office',
	'tourism/picnic',
	'tourism/terminal',
	'tourism/viewpoint',
	'tourism/wilderness_hut',
)
MARKERS = [(x, x) for x in MARKERS]

class Member(models.Model):
	first_name = models.CharField(_('first name'), max_length=50)
	surname = models.CharField(_('surname'), max_length=50)
	category = models.CharField(_('category'), max_length=5)
	email = models.EmailField(_('e-mail'), blank=True)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.surname)

	def email_special(self):
		return self.email.replace('@', '[zavinac]')

	class Meta:
		ordering = ('category','surname')
		verbose_name = _('member')
		verbose_name_plural = _('members')


class Event(MultilingualModel):
	title = models.CharField(_('title'), max_length=100)
	name = models.SlugField(
		_('name'),
		unique=True,
		help_text=_('Short name that will appear in the URL')
	)
	start_date = models.DateField(_('start date'))
	end_date = models.DateField(_('end date'), null=True, blank=True)
	location = models.CharField(_('location'), max_length=100)
	latitude = models.FloatField(_('latitude'), null=True, blank=True)
	longitude = models.FloatField(_('longitude'), null=True, blank=True)
	map_zoom = models.PositiveIntegerField(_('map zoom'),
		default=15,
		validators=[MaxValueValidator(19),]
	)
	category = models.ForeignKey(Category,
		verbose_name=_('category'),
		on_delete=models.CASCADE,
	)
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
	attachments = GenericRelation(Attachment)
	created = models.DateTimeField(_('created'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)

	def get_absolute_url(self):
		import ob.views
		return reverse(ob.views.event, kwargs={
			'lang': get_language(),
			'category_name': Category.objects.get(name_en='orienteering').name,
			'name': self.name,
		})

	def head_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.head))
		elif self.markup == 'textile': return mark_safe(textile(self.head))
		else: return mark_safe(self.head)

	def body_html(self):
		if self.markup == 'markdown': return mark_safe(markdown(self.body))
		elif self.markup == 'textile': return mark_safe(textile(self.body))
		else: return mark_safe(self.body)

	def is_upcoming(self):
		return self.end_date is None and self.start_date >= date.today() or \
			   self.end_date is not None and self.end_date >= date.today()

	def larger_map_link(self):
		import ob.views
		return None if self.mappoint_set.count() == 0 else \
		reverse(ob.views.event_map, kwargs={
			'lang': get_language(),
			'category_name': self.category.name,
			'name': self.name,
		})

	objects = MultilingualManager()

	class Meta:
		ordering = ('-start_date',)
		verbose_name = _('event')
		verbose_name_plural = _('events')
		translate = ('title', 'name', 'location', 'head', 'body')


class MapPoint(MultilingualModel):
	title = models.CharField(_('title'), max_length=100)
	latitude = models.FloatField(_('latitude'))
	longitude = models.FloatField(_('longitude'))
	marker = models.CharField(_('marker'),
		null=True,
		blank=True,
		max_length=100,
		choices=MARKERS,
	)
	event = models.ForeignKey(Event,
		verbose_name=_('event'),
		on_delete=models.CASCADE,
	)

	objects = MultilingualManager()

	class Meta:
		verbose_name = _('map point')
		verbose_name_plural = _('map points')
		translate = ('title',)
