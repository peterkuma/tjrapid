from __future__ import absolute_import
from news.app import News
from .models import Event
from datetime import date
from django.urls import reverse
from django.utils.translation import get_language
from main.models import Category

import ob.views

class OrienteeringNews(News):
    def archive(self, request, *args, **kwargs):
        events = sorted(Event.objects.all(), key=lambda event:
            abs((event.start_date - date.today()).days)
        )[0:2]

        events = sorted(events, key=lambda event:
            event.start_date
        )

        name = Category.objects.get(name_en='orienteering').name

        response = super(OrienteeringNews, self).archive(request, *args, **kwargs)
        response.template_name = 'ob/news/archive.html'
        response.context_data.update({
            'events': events,
            'events_url': reverse(ob.views.events, kwargs={
                'lang': get_language(),
                'category_name': name,
            }),
        })
        return response
