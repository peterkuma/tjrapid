from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'main.views.page', kwargs={'category_name': '', 'name': ''}, name='page'),
    url(r'^(?P<category_name>[^/]+)/$', 'main.views.page', kwargs={'name': ''}, name='page'),
    url(r'^(?P<category_name>[^/]+)/(?P<name>[^/]+)/$', 'main.views.page', name='page'),
    url(r'^(?P<category_name>[^/]+)/(?P<name>[^/]+)$','main.views.attachment', kwargs={'page_name': ''}, name='attachment'),
    url(r'^(?P<category_name>[^/]+)/(?P<page_name>[^/]+)/(?P<name>[^/]+)$','main.views.attachment', name='attachment'),
)
