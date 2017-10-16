from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode
from django.templatetags.static import StaticNode

from rangoapp.models.category import Category
from rango.settings import MEDIA_URL
register = template.Library()

@register.inclusion_tag('rangoapp/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
    'act_cat': cat}


@register.simple_tag()
def media(image=None):
    return MEDIA_URL+str(image)