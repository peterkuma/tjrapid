from django import template


register = template.Library()

@register.inclusion_tag('map.html')
def map(lon, lat, points=None, zoom=15, title=None, larger_map_link=None):
    if larger_map_link is None:
        larger_map_link = 'https://www.openstreetmap.org/?mlat={lat}amp;mlon={lon}#map={zoom}/{lat}/{lon}'.format(
            lon=lon,
            lat=lat,
            zoom=zoom,
        )
    return {
        'lon': lon,
        'lat': lat,
        'zoom': zoom,
        'title': title,
        'points': points,
        'larger_map_link': larger_map_link,
    }
