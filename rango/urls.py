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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.static import serve

from rangoapp.views.index import IndexViews
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#         url('^i18n/$', set_language, name='set_language'),
#
# ]
from rangoapp.views.user_profile import UserProfileCreateView

urlpatterns = i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexViews.as_view(), name='home'),
    url(r"^", include('rangoapp.urls')),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', login_required(logout), name='logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/activate/complete/$', UserProfileCreateView.as_view(),
        name='registration_activation_complete'),
    # url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    # url(r'^logout/$', login_required(logout), name='logout'),
    # url(r'', include('social.apps.django_app.urls', namespace='social')),
    # url(r'', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^doc/(.*)$', serve, {'document_root': settings.DOC_ROOT}),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.DOC_URL, document_root=settings.DOC_ROOT)
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.USE_MODELTRANSLATION:
#     urlpatterns += [
#         url('^i18n/$', set_language, name='set_language'),
#     ]
#
