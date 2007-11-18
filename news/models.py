from django.db import models
from django.utils.translation import ugettext as _

from tjrapid.main.models import *

class Article(models.Model):
	title = models.CharField(_('title'),max_length=100)
	category = models.ForeignKey(Category,verbose_name=_('category'))
	head = models.TextField(_('head'),blank=True)
	body = models.TextField(_('body'),blank=True)
	author = models.CharField(_('author'),max_length=100)
	published = models.DateTimeField(_('published'),auto_now_add=True)
	modified = models.DateTimeField(_('modified'),auto_now=True)
	
	def get_absolute_url(self):
		return '%snews/%s/%s/' % (self.category.get_absolute_url(), \
			self.published.strftime('%Y/%m/%d'),self.id)

	def path(self):
		return self.get_absolute_url()
		
	path.short_description = _("path")

	class Meta:
		get_latest_by = 'published',
		ordering = ('category','published')
		verbose_name = _('article')
		verbose_name_plural = _('articles')
	
	class Admin:
		list_display = ('title','category','path','published','author','modified')
		search_fields = ('name','title')
		list_filter = ('category','published','author')

