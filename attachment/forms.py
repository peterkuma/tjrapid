from django import forms
from django.contrib.contenttypes.generic import GenericInlineModelAdmin
from django.contrib.admin.templatetags.admin_static import static

from .models import Attachment

class AttachmentInline(GenericInlineModelAdmin):
    model = Attachment
    extra = 0
    template = 'admin/attachment_inline.html'

    @property
    def media(self):
        return forms.Media(
            js=[
                static('admin/js/d3.v3.min.js'),
                static('admin/js/attachment_inline.js'),
            ],
            css={'screen': [static('admin/css/attachment_inline.css')]},
        )
