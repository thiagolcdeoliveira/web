# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
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

class CategoryCreateView(SuccessMessageMixin,CreateView):
    model = Category
    form_class = CategoryForm
    success_message = "Categoria %(name)s cadastrada com sucesso! "

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        # messages.success(self.request, "Cadastrado com sucesso!", extra_tags='msg')
        return super(CategoryCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

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
