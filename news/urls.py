from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('tjrapid.news.views',
	(r'^$','archive'),
	(r'^(?P<year>\d{4})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','archive'),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$','details'),
)
