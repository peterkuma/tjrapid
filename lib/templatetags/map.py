from django import template


register = template.Library()

@register.inclusion_tag('map.html')
def map(lon, lat, zoom=15, border=True):
    return {
        'lon': lon,
        'lat': lat,
        'zoom': zoom,
    }
