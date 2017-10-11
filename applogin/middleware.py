from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import HttpResponse, render
from social import exceptions as social_exceptions
#
# class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
#     def process_exception(self, request, exception):
#         template="home.html"
#
#         if hasattr(social_exceptions, 'AuthCanceled'):
#             return render(request,template,{"mensagem":"Login Cancelado!"})
#         else:
#             raise exception
