from django.db import models

from datetime import date

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
	
	class Admin:
		list_display = ('surname','first_name','category','email')
		search_fields = ('first_name','surname')
		list_filter = ('category',)

class Competition(models.Model):
	title = models.CharField(_('title'),max_length=100)
	name = models.SlugField(
		_('name'),
		unique=True,
		prepopulate_from=('title',),
		help_text=_('Short name that will appear in the URL')
	)
	start_date = models.DateField(_('start date'))
	end_date = models.DateField(_('end date'),null=True,blank=True)
	location = models.CharField(_('location'),max_length=100,blank=True)
	specification = models.CharField(_('specification'),max_length=200,blank=True)
	results = models.CharField(_('results'),max_length=200,blank=True)
	photos = models.URLField(_('photos'),blank=True)
	
	def is_upcoming(self):
		return ((self.end_date is None and self.start_date >= date.today()) or (self.end_date is not None and self.end_date >= date.today()))
		#return ((type(self.end_date) == type(None) 
	
	class Meta:
		ordering = ('-start_date',)
		verbose_name = _('competition')
		verbose_name_plural = _('competitions')
		
	class Admin:
		list_display = ('title','start_date','end_date')
		search_fields = ('title','location')
		list_filter = ('start_date','location')
		js = ('/site_media/admin-ob_competitions.js',)

