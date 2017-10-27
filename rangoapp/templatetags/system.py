from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode
from django.shortcuts import get_object_or_404
from django.templatetags.static import StaticNode

from rangoapp.models.category import Category
from rango.settings import MEDIA_URL
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import calculate_position

register = template.Library()

@register.inclusion_tag('rangoapp/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
    'act_cat': cat}


@register.simple_tag()
def media(image=None):
    return MEDIA_URL+str(image)


@register.inclusion_tag('includes/user_card_tag.html')
def user_profile(user=None):
    context={}
    context["user_profile"] = get_object_or_404(UserProfile,user=user)
    context["position"] = calculate_position(context["user_profile"].points)
    #user_profile["lightning"] = 5
    return context
@register.inclusion_tag('includes/lightning.html')
# @register.simple_tag()
def lightning(points=None):
    context={}
    context["yellow"]= range(int(points))
    print(context["yellow"])
    context["gray"]=range(5-int(points))
    print(context["gray"])
    #user_profile["lightning"] = 5
    return context
