from django.conf.urls import url
from rangoapp.views.views import *
from rangoapp.views.category import *
from rangoapp.views.page import *
from rangoapp.views.user import *
from rangoapp.views.index import *




urlpatterns = [

    url(r'^home/$', IndexViews.as_view(), name='home'),
    url(r'^about/$', about, name='about'),
    # url(r'^add_category', add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #     show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
    #     add_page, name='add_page'),
    # url(r'^register', register, name='register'),

    # Category
    url(r'^category/cadastrar/$', CategoryCreateView.as_view(), name='category-add'),
    url(r'^category/visualizar/(?P<category_name_slug>[\w\-]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/editar/$', CategoryUpdateView.as_view(), name='category-update'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/excluir/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^category/listar/$', CategoryListView.as_view(), name='category-list'),
    
    # Page
    url(r'^category/(?P<category_name_slug>[\w\-]+)/page/cadastrar/$', PageCreateView.as_view(), name='page-add'),
    # url(r'^page/visualizar/(?P<page_name_slug>[\w\-]+)/$', PageDetailView.as_view(), name='page-detail'),
    url(r'^page/(?P<category_name_slug>[\w\-]+)/editar/$', PageUpdateView.as_view(), name='page-update'),
    url(r'^page/(?P<category_name_slug>[\w\-]+)/excluir/$', PageDeleteView.as_view(), name='page-delete'),
    url(r'^page/listar/$', PageListView.as_view(), name='page-list'),

    # User
    url(r'^user/cadastrar/$', UserCreateView.as_view(), name='user-add'),
    url(r'^user/visualizar/(?P<username>[\w\-]+)/$', UserDetailView.as_view(),
        name='user-detail'),
    url(r'^user/(?P<username>[\w\-]+)/category/listar/$', CategoryListByUserView.as_view(),
        name='user-category-list'),
    # url(r'^user/(?P<user_name_slug>[\w\-]+)/editar/$', UserUpdateView.as_view(), name='user-update'),
    # url(r'^user/(?P<user_name_slug>[\w\-]+)/excluir/$', UserDeleteView.as_view(), name='user-delete'),
    # url(r'^user/listar/$', UserListView.as_view(), name='user-list'),

]