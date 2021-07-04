import re
import markdown as md
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def map(lon, lat, dlon=0.01, dlat=0.01, zoom=15, border=True):
    return mark_safe('''<div style="position: relative; width: 100%; height: 100%"><iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox={lon1}%2C{lat1}%2C{lon2}%2C{lat2}&amp;layer=mapnik&amp;marker={lat}%2C{lon}" style="border: 1px solid black; width: 100%; height: 100%"></iframe><div style="position: absolute; top: 0; right: 0; background: #ffffffaa; padding: 2px 4px"><small><a style="text-decoration: none" href="https://www.openstreetmap.org/?mlat={lat}&amp;mlon={lon}#map={zoom}/{lat}/{lon}&amp">View larger map</a></small></div></div>'''.format(
        lon1=('%.15f' % (lon - dlon)),
        lat1=('%.15f' % (lat - dlat)),
        lon2=('%.15f' % (lon + dlon)),
        lat2=('%.15f' % (lat + dlat)),
        lon=('%.15f' % lon),
        lat=('%.15f' % lat),
        zoom=zoom,
    ))
