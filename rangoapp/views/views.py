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
                # return redirect(reverse("show_category", kwargs={"category_name_slug":category_name_slug}))
                return HttpResponseRedirect(reverse('show_category', args=[category_name_slug]))
                # return HttpResponseRedirect(reverse('show_category', kwargs={"category_name_slug":category_name_slug}))

                # return redirect(reverse("show_category", kwargs={"category_name_slug":category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'rango/register.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})
