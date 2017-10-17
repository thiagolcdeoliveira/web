"""rango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.shortcuts import render

from rangoapp.views.index import IndexViews
from registration.backends.simple.views import RegistrationView
# class MyRegistrationView(RegistrationView):
#       def get_success_url(self, request, user=None):
#             return '/'
from rangoapp.views.user import MyRegistrationView
def handle404(request):
    return render(request, '404.html', {})


def handle403(request):
    return render(request, '403.html', {})


def handle500(request):
    return render(request, '500.html', {})
urlpatterns = [
      url(r'^$', IndexViews.as_view(), name='home'),
      # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
      # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
      url(r'^admin/', admin.site.urls),
      url(r"^rango/", include('rangoapp.urls')),
      url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
      url(r'^logout/$', login_required(logout), name='logout'),
      url(r'', include('social.apps.django_app.urls', namespace='social')),
      url(r'', include('django.contrib.auth.urls', namespace='auth')),
      # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
      # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),

      url(r'^accounts/', include('registration.backends.default.urls')),
      # url(r'^', handle404, name='404'),
      # url(r'^', handle403, name='403'),
      # url(r'^', handle500, name='500'),


      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
