# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Peter Kuma

from django.contrib import admin

from models import *

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'open_date', 'close_date')

class AccommodationAdmin(admin.ModelAdmin):
	list_display = ('id', 'event', '__unicode__', 'capacity')
	list_filter = ('event',)

class ClassFeeAdmin(admin.ModelAdmin):
	list_display = ('event', 'label', 'classes')
	list_filter = ('event',)

class EntryAdmin(admin.ModelAdmin):
	list_display = ('event', 'id', 'email')
	list_filter = ('event',)

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('entry', 'id', 'firstname', 'surname', 'cls')
	list_filter = ('entry',)

class DirectoryAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'surname', 'club', 'cls')
	list_filter = ('cls',)

admin.site.register(Event, EventAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(ClassFee, ClassFeeAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Directory, DirectoryAdmin)

