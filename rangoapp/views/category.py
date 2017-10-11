# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic import *

from rangoapp.models.category import Category
from rangoapp.forms.category import CategoryForm
from rangoapp.models.page import Page


class CategoryListView(ListView):
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'category_name_slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        print(self.kwargs['category_name_slug'])
        context['pages'] = Page.objects.filter(category__slug=self.kwargs['category_name_slug'])
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CategoryCreateView, self).form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    # form_class = CategoryEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CategoryUpdateView, self).form_valid(form)


class CategoryDeleteView(DeleteView):
    queryset = Category.objects.all()
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(CategoryDeleteView, self).form_valid(form)
