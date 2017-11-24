# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.models.category import Category
from rangoapp.forms.category import CategoryForm
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.permission.decorators import profile_required
from rangoapp.views.ranking import add_points_category, add_points_like_category, remove_points_like_category, \
    remove_points_deslike_category, \
    add_points_deslike_category, remove_points_category
from django.utils.translation import ugettext_lazy as _


@method_decorator(profile_required, name='dispatch')
class CategoryListView(ListView):
    '''
     Lista todos as categorias.
    :URl: http://ip_servidor/category/listar/
    '''
    queryset = Category.objects.all()

    def get_queryset(self):
        '''
         Define a consulta a ser feita.
        :return: Categorias do usuário logado
        '''
        queryset = super(CategoryListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        '''
         Define o contexto a ser enviado para página.
        
        :return: Adiciona ao contexto categories (categorias do usuário logado) e profile_request (perfil do usuário logado)
        '''
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context["categories"] = self.get_queryset()
        context["profile_request"] = get_object_or_404(UserProfile, user=self.request.user)

        return context


class CategoryListByUserView(ListView):
    '''
     Lista todos as categorias por usuário especifico.
    :URl: http://ip_servidor/user/<username>/category/listar/
    '''
    queryset = Category.objects.all()

    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # template_name =

    def get_queryset(self):
        '''
        Define a consulta a ser feita.
        :return: Categorias do usuário selecionado.
        '''
        queryset = super(CategoryListByUserView, self).get_queryset()
        queryset = queryset.filter(is_private=False, user__username=self.kwargs["username"])
        print (queryset)
        return queryset

    def get_context_data(self, **kwargs):
        '''
         Define o contexto a ser enviado para página.
        :return: Adiciona ao contexto categories (categorias do usuário selecionado) e profile_request (perfil do usuário selecionado)
        '''

        context = super(CategoryListByUserView, self).get_context_data(**kwargs)
        context["categories"] = self.queryset
        context["profile_request"] = get_object_or_404(UserProfile, user=self.request.user)

        return context


# permissao na categoory
class CategoryDetailView(DetailView):
    '''
     Detalhes da categoria.
    :URl: http://ip_servidor/category/visualizar/<category_name_slug>/
    '''

    queryset = Category.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'category_name_slug'

    def get_context_data(self, **kwargs):
        '''
         Define o contexto a ser enviado para página.
        :return: Adiciona ao contexto pages (páginas da categoria selecionada) e profile_request (perfil do usuário logado)
        '''
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(category__slug=self.kwargs['category_name_slug'])
        context['profile_request'] = get_object_or_404(UserProfile, user=self.request.user)
        return context


class CategoryCreateView(SuccessMessageMixin, CreateView):
    '''
     Cria  categoria.
    :URl: http://ip_servidor/category/cadastrar/
    '''
    model = Category
    form_class = CategoryForm
    success_message = _("Category %(name)s added with successfull! ")

    def form_valid(self, form):
        '''
         Valida o form. 
        Se categoria for publica (não privada) adicioana os pontos.
        '''
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if not self.object.is_private:
            add_points_category(self.request.user)
        self.object.save()
        # messages.success(self.request, "Cadastrado com sucesso!", extra_tags='msg')
        return super(CategoryCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        '''
         Define mensagem de sucesso.
        :return: categoria <nome> cadastrada com sucesso.
        '''
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    '''
     Atualiza a categoria.
    :URl: http://ip_servidor/category/<category_name_slug>/editar/
    '''
    model = Category
    form_class = CategoryForm
    slug_field = 'slug'
    slug_url_kwarg = 'category_name_slug'
    success_message = _("Category %(name)s changed with successfull! ")

    # form_class = CategoryEditForm

    def form_valid(self, form):
        '''
         Valida o form. 
        '''
        self.object = form.save(commit=False)
        self.object.save()
        return super(CategoryUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        '''
         Define mensagem de sucesso.
        :return: categoria <nome> cadastrada com sucesso.
        '''
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    '''
     Deleta a categoria.
    :URl: http://ip_servidor/category/listar/
    '''
    queryset = Category.objects.all()
    success_url = reverse_lazy('category-list')
    slug_field = 'slug'
    slug_url_kwarg = 'category_name_slug'
    success_message = _("Category  deleted with successfull! ")

    def form_valid(self, form):
        '''
         Valida o form. 
        Se categoria for publica (não privada) remove os pontos.
        '''

        self.object = form.save(commit=False)
        self.object.save()
        if not self.object.is_private:
            remove_points_category(self.object.user)
        return super(CategoryDeleteView, self).form_valid(form)

    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)
    def get_success_message(self, cleaned_data):
        '''
         Define mensagem de sucesso.
        :return: categoria <nome> cadastrada com sucesso.
        '''
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )



def set_like_category(request):
    '''
     Define o like para categoria.
    :URl: http://ip_servidor/category/like/
    '''
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
    '''
     Define o deslike para categoria.
    :URl: http://ip_servidor/category/deslike/
    '''
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
