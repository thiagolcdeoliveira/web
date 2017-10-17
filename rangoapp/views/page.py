# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.forms.page import PageForm
from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.views.ranking import addPointsPage


class PageListView(ListView):
    queryset = Page.objects.all()


class PageCreateView(SuccessMessageMixin,CreateView):
    model = Page
    form_class = PageForm
    success_message = u"Página %(name)s cadastrada com sucesso! "

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.category=get_object_or_404(Category,slug=self.kwargs["category_name_slug"])
        self.object.save()
        addPointsPage(self.request.user)
        # messages.success(self.request, "Cadastrado com sucesso!", extra_tags='msg')
        return super(PageCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.title,
        )

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    # form_class = PageEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(PageUpdateView, self).form_valid(form)


class PageDeleteView(DeleteView):
    queryset = Page.objects.all()
    success_url = reverse_lazy('page-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(PageDeleteView, self).form_valid(form)
