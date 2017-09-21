# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World! <a href = '/rango/about/'>about</a>")
#
# def about(request):
#     return HttpResponse("Hello World! <a href= '/rango/home/'>home</a> ")
from rangoapp.models import Category, Page


def index(request):
    context_dict = {}
    bold_message = 'E aí, BSI, tudo em cima?'
    autor = 'Thiago'
    context_dict['bold_message'] = bold_message
    context_dict['autor'] = autor

    return render(request, 'rango/index.html', context_dict)

def about(request):

    return render(request, 'rango/about.html', {'autor':'Thiago'})
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)