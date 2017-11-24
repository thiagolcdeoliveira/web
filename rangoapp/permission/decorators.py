# coding=utf-8
# from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from rangoapp.models.category import Category
from rangoapp.models.page import Page


# from appusuario.models import ComplementoUsuario
from rangoapp.models.user_profile import UserProfile


def is_owner_submissao(object, permission):
    def _dec(func):
        def _new_func(request, *args, **kwargs):
            if object.get(pk=kwargs['pk']).usuario == request.user or request.user.has_perm(
                    permission) or request.user in object.get(pk=kwargs['pk']).autores.all():
                return func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return _new_func

    return _dec


def is_ownerpage(permission):
    '''
    Verifica se o usuário logado possui autorizaçõa para acessar sua função, ou seja 
    se le possui a permissão adquada, é o criador do objeto ou um dos autores. 
    '''

    def _dec(func):
        def _new_func(request, *args, **kwargs):
            object = get_object_or_404(Category, slug=kwargs['category_name_slug'])
            if object.user == request.user or request.user.has_perm(permission):
                return func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return _new_func

    return _dec


def profile_required(func):
    """
    Verifica se possui um perfil, caso contário retorna para adicionar perfil.
    """

    def _decorated(request, *args, **kwargs):
        profile = UserProfile.objects.filter(user=request.user)
        if not profile:
            return redirect(reverse("user-profile-add"))
        # if not request.user.is_authenticated:
        #     context={}
        #     context["message"]= True
        #     context["next"]=request.path
        #     return render(request,'home.html',context)

        return func(request, *args, **kwargs)

    return _decorated
