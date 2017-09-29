# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World! <a href = '/rango/about/'>about</a>")
#
# def about(request):
#     return HttpResponse("Hello World! <a href= '/rango/home/'>home</a> ")
from rangoapp.forms import PageForm, CategoryForm
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
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
        print(category.name)
    except Category.DoesNotExist:
        category = None
        print (category_name_slug, 'não existe')
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                # return show_category(request, category_name_slug)
                return redirect(reverse("show_category",kwargs=category_name_slug))
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)