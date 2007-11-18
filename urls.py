from django.conf.urls.defaults import *
from django.conf import settings

from tjrapid.main.models import Category
from tjrapid.ob.models import Member
from tjrapid.settings import *

urlpatterns = patterns('',
    (r'^admin/',include('django.contrib.admin.urls')),
    (r'^ob/clenovia/$','tjrapid.ob.views.members',dict(category_name='ob')),
    (r'^en/orienteering/members/$','tjrapid.ob.views.members',dict(category_name='orienteering')),
    (r'^ob/preteky/$','tjrapid.ob.views.competitions',dict(category_name='ob')),
    (r'^en/orienteering/competitions/$','tjrapid.ob.views.competitions',dict(category_name='orienteering')),
    (r'^([^/]*)/?$','tjrapid.main.views.page'),
    (r'^([^/]*)/([^/]*)/$','tjrapid.main.views.page'),
    (r'^([^/]*)/([^/]*)/([^/]*)/$','tjrapid.main.views.page'),
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    ) 
