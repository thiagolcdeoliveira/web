from django.conf.urls import url
from rangoapp.views.views import *
from rangoapp.views.category import *
urlpatterns = [

    url(r'^home/$', index, name='home'),
    url(r'^about/$', about, name='about'),
    # url(r'^add_category', add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #     show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
    #     add_page, name='add_page'),
    url(r'^register', register, name='register'),

    # Category
    url(r'^category/cadastrar/$', CategoryCreateView.as_view(), name='category-add'),
    url(r'^category/visualizar/(?P<category_name_slug>[\w\-]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/editar/$', CategoryUpdateView.as_view(), name='category-update'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/excluir/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^category/listar/$', CategoryListView.as_view(), name='category-list'),

]