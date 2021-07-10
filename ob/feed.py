import datetime as dt
import pytz

from news.feed import NewsFeed
from news.models import Article
from ob.models import Event

TZ = pytz.timezone('Europe/Bratislava')

class OrienteeringNewsFeed(NewsFeed):
    def item_author(self, item):
        return '' if type(item) is Event else \
            NewsFeed.item_author(self, item)

    def item_pubdate(self, item):
        return TZ.localize(dt.datetime.fromordinal(item.start_date.toordinal())) \
            if type(item) is Event else \
            NewsFeed.item_pubdate(self, item)

    def item_description(self, item):
        return '' if type(item) is Event else \
            NewsFeed.item_description(self, item)

    def items(self, obj):
        return sorted(
            list(Article.objects.filter(category=obj).exclude(title='')) + \
            list(Event.objects.filter(category=obj)),
            key=lambda o: \
                TZ.localize(dt.datetime.fromordinal(o.start_date.toordinal())) \
                if type(o) is Event \
                else o.published,
            reverse=True
        )
