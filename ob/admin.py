# -*- coding: utf-8 -*-
#
# $Id$
#
# Copyright (c) 2010 Peter Kuma
# All rights reserved.
#

from models import *
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
	list_display = ('surname','first_name','category','email')
	search_fields = ('first_name','surname')
	list_filter = ('category',)

class CompetitionAdmin(admin.ModelAdmin):
	list_display = ('title','start_date','end_date')
	search_fields = ('title','location')
	list_filter = ('start_date','location')
	js = ('/site_media/admin-ob_competitions.js',)

admin.site.register(Member, MemberAdmin)
admin.site.register(Competition, CompetitionAdmin)

