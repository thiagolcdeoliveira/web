from django.conf.urls import url
from rangoapp.views import *

urlpatterns = [

    url(r'^home/$', index, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        show_category, name='show_category'),
]