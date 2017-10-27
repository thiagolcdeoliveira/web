# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.models.category import Category
from rangoapp.forms.category import CategoryForm
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import add_points_category, add_points_like_category, remove_points_like_category, remove_points_deslike_category, \
    add_points_deslike_category


class CategoryListView(ListView):
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CategoryListByUserView(ListView):
    queryset = Category.objects.all()

    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # template_name =

    def get_queryset(self):
        queryset = super(CategoryListByUserView, self).get_queryset()
        queryset = queryset.filter(is_private=False, user__username=self.kwargs["username"])
        print (queryset)
        return queryset


# permissao na categoory
class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'category_name_slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(category__slug=self.kwargs['category_name_slug'])
        context['profile_request'] = get_object_or_404(UserProfile,user=self.request.user)
        return context


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_message = "Categoria %(name)s cadastrada com sucesso! "

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if not self.object.is_private:
            add_points_category(self.request.user)
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
        if not self.object.is_private:
            remove_points_category(self.object.user)
        return super(CategoryDeleteView, self).form_valid(form)

    #

    # def set_like(request):
    #     data = {}
    #     category_slug = request.GET.get('category')
    #     profile = get_object_or_404(UserProfile,user=request.user)
    #     category_like =UserProfile.objects.filter(user=request.user,category_like__slug__in=[category_slug])
    #     category = get_object_or_404(Category, slug=category_slug)
    #
    #     # print(category)
    #     if not category_like:
    #         profile.category_like.add(category)
    #         addPointsLike(category.user)
    #         category.likes+=1
    #         category.save()
    #         data["message"]=True
    #         data['likes'] = category.likes
    #         data['is_like'] = True
    #     else:
    #         # data["message"]=True
    #
    #         profile.category_like.remove(category)
    #         category.likes-=1
    #         category.save()
    #         profile.save()
    #         data["message"] = False
    #         # data["message"] = True
    #         data['likes'] = category.likes
    #         data['is_likes'] = False
    #         removePointsLike(category.user)
    #
    #     return JsonResponse(data)

    # data = {
    #     'message': 'success',
    #
    # }


# return JsonResponse(data)


def set_like_category(request):
    data = {}
    category_slug = request.GET.get('category')
    profile = get_object_or_404(UserProfile, user=request.user)
    user = UserProfile.objects.filter(user=request.user)
    category_like = user.filter(category_like__slug__in=[category_slug])
    category = get_object_or_404(Category, slug=category_slug)
    category_deslike = user.filter(category_deslike__slug__in=[category_slug])
    # print(category)
    if not category_deslike:
        data["message"] = True

        if not category_like:
            profile.category_like.add(category)
            add_points_like_category(category.user)
            category.likes += 1
            category.save()
            data['likes'] = category.likes
            data['is_like'] = True
        else:
            # data["message"]=True

            profile.category_like.remove(category)
            category.likes -= 1
            category.save()
            profile.save()
            # data["message"] = True
            data['likes'] = category.likes
            data['is_likes'] = False
            remove_points_like_category(category.user)
    else:
        data["message"] = False

    return JsonResponse(data)


def set_deslike_category(request):
    data = {}
    category_slug = request.GET.get('category')
    profile = get_object_or_404(UserProfile, user=request.user)
    user = UserProfile.objects.filter(user=request.user)
    category_deslikes = user.filter(category_deslike__slug__in=[category_slug])
    category = get_object_or_404(Category, slug=category_slug)
    category_likes = user.filter(category_like__slug__in=[category_slug])

    if not category_likes:
        data["message"] = True

        if not category_deslikes:
            profile.category_deslike.add(category)
            add_points_deslike_category(category.user)
            category.deslikes += 1
            category.save()
            data['deslikes'] = category.deslikes
            data['is_deslike'] = True
        else:
            # data["message"]=True
            profile.category_deslike.remove(category)
            category.deslikes -= 1
            category.save()
            profile.save()
            data['deslikes'] = category.deslikes
            data['is_deslikes'] = False
            remove_points_deslike_category(category.user)
    else:
        data["message"] = False

    return JsonResponse(data)
