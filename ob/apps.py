from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ObAppConfig(AppConfig):
    name = 'ob'
    verbose_name = _('Orienteering')
