# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.forms.page import PageForm
from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.permission.decorators import is_ownerpage, profile_required
from rangoapp.views.ranking import add_points_page, add_points_like_page, remove_points_like_page, \
    add_points_deslike_page, remove_points_deslike_page, remove_points_category, remove_points_page
from django.utils.translation import ugettext_lazy as _
from rangoapp.variaveis.variaveis import ADD_PAGE


@method_decorator(profile_required, name='dispatch')
class PageListView(ListView):
    '''
     Lista todos as categorias.
    :URl: http://ip_servidor/page/listar/
    '''
    queryset = Page.objects.all()

    def get_queryset(self):
        '''
         Define a consulta a ser feita.
        :return: páginas do usuário logado
        '''
        queryset = super(PageListView, self).get_queryset()
        queryset = queryset.filter(category__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        '''
         Define o contexto a ser enviado para página.
        :return: Adiciona ao contexto pages (páginas do usuário logado) e profile_request (perfil do usuário logado)
        '''
        context = super(PageListView, self).get_context_data(**kwargs)
        context["pages"] = self.get_queryset()
        context["profile_request"] = get_object_or_404(UserProfile, user=self.request.user)


class PageDetailViews(DetailView):
    '''
     Detalhes da categoria.
    :URl: http://ip_servidor/user/page/<id>/
    '''
    queryset = Page.objects.all()


    def get(self, request, *args, **kwargs):
        '''
         Define o o redirecionamento da pagiona baseado no id da página.
        :return: Redirenciona para o link correspondente ao id da página
        '''
        page = get_object_or_404(Page, id=kwargs["id"])
        page.views += 1
        page.save()

        # print (page.url)
        # return redirect("http://www.google.com")
        return redirect(page.url)

        # return redirect(self.object.url)
        # return redirect(self.object.url)


@method_decorator(is_ownerpage(ADD_PAGE), name='dispatch')
class PageCreateView(SuccessMessageMixin, CreateView):
    '''
     Adiciona uma página na categoria.
    :URl: http://ip_servidor/category/<category_name_slug>/page/cadastrar/
    '''
    model = Page
    form_class = PageForm
    success_message = _("Page %(name)s added with successufull!")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.category = get_object_or_404(Category, slug=self.kwargs["category_name_slug"])
        self.object.save()
        if not self.object.category.is_private:
            add_points_page(self.request.user)
        return super(PageCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.title,
        )

class PageListByUserView(ListView):
    '''
     Lista páginas por usuario.
    :URl: http://ip_servidor/user/<username>/page/listar
    '''

    queryset = Page.objects.all()

    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # template_name =

    def get_queryset(self):
        '''
         Define a consulta a ser feita.
        :return Páginas do usuário logado
        '''
        queryset = super(PageListByUserView, self).get_queryset()
        queryset = queryset.filter(category__is_private=False, category__user__username=self.kwargs["username"])
        print (queryset)
        return queryset

    def get_context_data(self, **kwargs):
        '''
         Define o contexto a ser enviado para página.

        :return: Adiciona ao contexto pages (páginas de um usuário) e profile_request (perfil do usuário logado)
       '''
        context = super(PageListByUserView, self).get_context_data(**kwargs)
        context["pages"] = self.queryset
        context["profile_request"] = get_object_or_404(UserProfile, user=self.request.user)


class PageUpdateView(SuccessMessageMixin, UpdateView):
    '''
     Atualiza uma página.
    :URl: http://ip_servidor/category/listar/
    '''
    model = Page
    form_class = PageForm
    success_message = _("Page %(name)s changed with successufull!")

    # form_class = PageEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(PageUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.title,
        )


class PageDeleteView(SuccessMessageMixin, DeleteView):
    '''
     Deletar uma página.
    :URl: http://ip_servidor/page/<pk>/excluir
    '''
    success_message = _("Page %(name)s deleted with successufull!")

    queryset = Page.objects.all()
    success_url = reverse_lazy('page-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        if not self.object.category.is_private:
            remove_points_page(self.object.category.user)
        return super(PageDeleteView, self).form_valid(form)

    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.title,
        )
def set_like_page(request):
    data = {}
    page_id = request.GET.get('page')
    print("aqui")
    profile = get_object_or_404(UserProfile, user=request.user)
    user = UserProfile.objects.filter(user=request.user)
    page_like = user.filter(page_like__id__in=[page_id])
    page = get_object_or_404(Page, id=page_id)
    page_deslike = user.filter(page_deslike__id__in=[page_id])
    # print(category)
    print("aqui %s" % page_id)
    if not page_deslike:
        data["message"] = True

        if not page_like:
            profile.page_like.add(page)
            add_points_like_page(page.category.user)
            page.likes += 1
            page.save()
            data['likes'] = page.likes
            data['is_like'] = True
        else:
            # data["message"]=True

            profile.page_like.remove(page)
            page.likes -= 1
            page.save()
            profile.save()
            # data["message"] = True
            data['likes'] = page.likes
            data['is_likes'] = False
            remove_points_like_page(page.category.user)
    else:
        data["message"] = False

    return JsonResponse(data)


def set_deslike_page(request):
    data = {}
    page_id = request.GET.get('page')
    profile = get_object_or_404(UserProfile, user=request.user)
    user = UserProfile.objects.filter(user=request.user)
    print(user)
    page_deslikes = user.filter(page_deslike__id__in=[page_id])
    page = get_object_or_404(Page, id=page_id)
    print(page)
    page_likes = user.filter(page_like__id__in=[page_id])

    if not page_likes:
        data["message"] = True

        if not page_deslikes:
            profile.page_deslike.add(page)
            add_points_deslike_page(page.category.user)
            page.deslikes += 1
            page.save()
            data['deslikes'] = page.deslikes
            data['is_deslike'] = True
        else:
            # data["message"]=True
            profile.page_deslike.remove(page)
            page.deslikes -= 1
            page.save()
            profile.save()
            data['deslikes'] = page.deslikes
            data['is_deslikes'] = False
            remove_points_deslike_page(page.category.user)
    else:
        data["message"] = False

    return JsonResponse(data)
