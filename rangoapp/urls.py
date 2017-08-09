from django.conf.urls import url
from rangoapp.views import *

urlpatterns = [

    url(r'^home/$', index, name='home'),
    url(r'^about/$', about, name='about'),

]