# coding=utf-8
# from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rangoapp.models.category import Category
from rangoapp.models.page import Page


# from appusuario.models import ComplementoUsuario


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
