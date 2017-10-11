from django import template
from rangoapp.models.category import Category

register = template.Library()

@register.inclusion_tag('rango/../../templates/rangoapp/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
    'act_cat': cat}