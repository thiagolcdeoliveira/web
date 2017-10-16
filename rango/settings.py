# coding=utf-8
"""
Django settings for rango project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import smtplib
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#rx6=ne$1dwk4!hb985qw!0sqm*le3ya=nzk_#@g)txf0y5=l^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    'django.contrib.admin',
   # 'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rangoapp',
    'registration',
    'social.apps.django_app.default',
    'social_django',


    #'applogin',
]
# SITE_ID=1
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
REGISTRATION_EMAIL_HTML = False    # and are trying to access pages requiring authentication

#
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# then i tried using my own address and smtp.live.com

# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# REGISTRATION_AUTO_LOGIN = True #
REGISTRATION_DEFAULT_FROM_EMAIL ="noreplay@starlabs.com"
# REGISTRATION_DEFAULT_FROM_EMAIL ="thiagolocatellicdeoliveira@gmail.com"
#
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'rango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


            ],
        },
    },
]

WSGI_APPLICATION = 'rango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# LANGUAGE_CODE = 'pt-br'
#
# TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
#Media files
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# --- INÍCIO AUTENTICAÇÃO COM AS REDE SOCIAIS ----#

LANGUAGES = (
    ('en', u'Inglês'),
    ('pt-br', u'Português'),
    ('es', u'Espanhol'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOAuth2',
)

# --- END AUTENTICAÇÃO COM AS REDE SOCIAIS ----#

# --- URL -----#
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
LOGIN_ERROR_URL = '/'

# --------AND URLs-----#

# --- Valores que precisam ser alteardos ----#

# Troque a chave do gmail https://console.developers.google.com/apis/dashboard?project=login-164921&duration=PT1H
# https://console.developers.google.com/apis/credentials?project=login-164921
# http://python-social-auth.readthedocs.io/en/latest/index.html
#
SOCIAL_AUTH_GITHUB_KEY = '86679a8d96ef69438aee'
SOCIAL_AUTH_GITHUB_SECRET = '976b810bed9a16d3234043c2cb0650553c7e35fc'
SOCIAL_AUTH_FACEBOOK_KEY = '141165153076797'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '01a65ccaf83c6bbc7a73546bd8240d36'  #
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '71535515086-1ljbb4p2th9kvqrror6rpv7r7002g56v.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'lJIXT9jAH1wsMZGmqhwdl-sb'
SOCIAL_AUTH_TWITTER_KEY = 'QSb7mvQtBf4SaVR6gwp1CTJcd'
SOCIAL_AUTH_TWITTER_SECRET = 'fjR9FhKQHrdaP5JD66SeaUpX0QADh0ixgnNALwUxDJ7XuMvDwJ'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# ============================