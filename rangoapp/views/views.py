# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World! <a href = '/rango/about/'>about</a>")
#
# def about(request):
#     return HttpResponse("Hello World! <a href= '/rango/home/'>home</a> ")
from rangoapp.forms.category import  CategoryForm
from rangoapp.forms.page import PageForm
from rangoapp.forms.user import UserProfileForm, UserForm
from rangoapp.models.category import Category
from rangoapp.models.page import  Page
from rangoapp.models.user_profile import UserProfile


def index(request):
    context_dict = {}
    bold_message = 'E aí, BSI, tudo em cima?'
    autor = 'Thiago'
    context_dict['bold_message'] = bold_message
    context_dict['autor'] = autor
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories'] = category_list

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    return render(request, 'rangoapp/index.html', context_dict)

def about(request):

    return render(request, 'rangoapp/about.html', {'autor': 'Thiago'})