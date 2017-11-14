from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from rangoapp.views.user_profile import *
from rangoapp.views.views import *
from rangoapp.views.category import *
from rangoapp.views.page import *
from rangoapp.views.user import *
from rangoapp.views.index import *





urlpatterns = [

    url(r'^home/$', IndexViews.as_view(), name='home'),
    url(r'^about/$', about, name='about'),

    # Category
    url(r'^category/cadastrar/$', CategoryCreateView.as_view(), name='category-add'),
    url(r'^category/visualizar/(?P<category_name_slug>[\w\-]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/editar/$', CategoryUpdateView.as_view(), name='category-update'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/excluir/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^category/listar/$', CategoryListView.as_view(), name='category-list'),
    # url(r'^category/(?P<username>[\w\-]+)/listar/$', CategoryListByUsernameView.as_view(), name='category-list-username'),
    url(r'^category/like/$', set_like_category, name='category-set-like'),
    url(r'^category/deslike/$', set_deslike_category, name='category-set-deslike'),

    # Page
    url(r'^category/(?P<category_name_slug>[\w\-]+)/page/cadastrar/$', PageCreateView.as_view(), name='page-add'),
    url(r'^page/(?P<pk>[\d\-]+)/editar/$', PageUpdateView.as_view(), name='page-update'),
    url(r'^page/(?P<category_name_slug>[\w\-]+)/excluir/$', PageDeleteView.as_view(), name='page-delete'),
    url(r'^page/listar/$', PageListView.as_view(), name='page-list'),
    url(r'^page/like/$', set_like_page, name='page-set-like'),
    url(r'^page/deslike/$', set_deslike_page, name='page-set-deslike'),
    # User
    url(r'^user/cadastrar/$', UserCreateView.as_view(), name='user-add'),
    url(r'^user/(?P<username>[\w\-]+)/update/$', UserUpdateView.as_view(), name='user-update'),
    url(r'^user/visualizar/(?P<username>[\w\-]+)/$', UserDetailView.as_view(),
        name='user-detail'),
    url(r'^user/visualizar/(?P<username>[\w\-]+)/update/$', UserChangeDetailView.as_view(),
        name='user-change-detail'),
    url(r'^user/(?P<username>[\w\-]+)/category/listar/$', CategoryListByUserView.as_view(),
        name='user-category-list'),
    url(r'^user/(?P<username>[\w\-]+)/page/listar/$', PageListByUserView.as_view(),
        name='user-page-list'),
    url(r'^user/page/(?P<id>[\d\-]+)/$', PageDetailViews.as_view(),
            name='page-detail'),
    # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),

    # url(r'^user/(?P<user_name_slug>[\w\-]+)/editar/$', UserUpdateView.as_view(), name='user-update'),
    # url(r'^user/(?P<user_name_slug>[\w\-]+)/excluir/$', UserDeleteView.as_view(), name='user-delete'),
    # url(r'^user/listar/$', UserListView.as_view(), name='user-list'),
    url(r'^userprofile/cadastrar/$', UserProfileCreateView.as_view(), name='user-profile-add'),
    # url(r'^userprofile/(?P<username>[\w\-]+)/update/$', UserProfileUpdateView.as_view(), name='user-profile-update'),
    url(r'^userprofile/(?P<pk>[\d\-]+)/update/$', UserProfileUpdateView.as_view(), name='user-profile-update'),
    url(r'^user/(?P<pk>[\d\-]+)/delete/$', UserDeleteView.as_view(), name='user-delete'),
    url(r'^user/friend/$', set_friend, name='user-delete'),



]