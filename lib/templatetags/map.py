import re
import markdown as md
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def map(lon, lat, zoom=15, border=True):
    return mark_safe('''<div style="position: relative; width: 100%; height: 100%; border: 1px solid #aaa">
<div style="width: 100%; height: 100%"><script>
var el = document.getElementsByTagName('script');
el = el[el.length - 1].parentNode;
var map = L.map(el).setView([{lat}, {lon}], {zoom});
map.attributionControl.setPrefix('');
L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}}).addTo(map);
L.marker([{lat}, {lon}]).addTo(map);
</script></div>
<div style="position: absolute; top: 0; right: 0; z-index: 1000; background: #ffffffaa; padding: 2px 4px"><small><a style="text-decoration: none" href="https://www.openstreetmap.org/?mlat={lat}&amp;mlon={lon}#map={zoom}/{lat}/{lon}&amp">View larger map</a></small></div></div>'''.format(
        lon=('%.15f' % lon),
        lat=('%.15f' % lat),
        zoom=zoom,
    ))
