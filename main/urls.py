from django.conf.urls import re_path

import main.views

urlpatterns = [
    re_path(r'^$', main.views.page, kwargs={'category_name': '', 'name': ''}, name='page'),
    re_path(r'^(?P<category_name>[^/]+)/$', main.views.page, kwargs={'name': ''}, name='page'),
    re_path(r'^(?P<category_name>[^/]+)/(?P<name>[^/]+)/$', main.views.page, name='page'),
    re_path(r'^(?P<category_name>[^/]+)/(?P<name>[^/]+)$',main.views.attachment, kwargs={'page_name': ''}, name='attachment'),
    re_path(r'^(?P<category_name>[^/]+)/(?P<page_name>[^/]+)/(?P<name>[^/]+)$',main.views.attachment, name='attachment'),
]
