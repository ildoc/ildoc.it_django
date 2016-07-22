# -*- coding: utf-8 -*-
# Django settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v6@x8_-sz%#(b^vq879z*x7tcivq)$1yv-5f8@slqnf5c+13n2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

THIRDPART_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    'pagedown',
    # 'rest_framework',
]

PROJECT_APPS = [
    'blog.apps.BlogConfig',
    'quotes.apps.QuotesConfig',
    # 'snippets',
]

INSTALLED_APPS = PREREQ_APPS + THIRDPART_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ildoc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'core.context_processors.core_values',
                'blog.context_processors.blog_common',
                'quotes.context_processors.quotes_common',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

LOGIN_REDIRECT_URL = "/"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'it_IT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Absolute path to the directory that holds media.
# Example: '/home/media/media.lawrence.com/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: 'http://media.lawrence.com', 'http://example.com/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files like app media.
# Example: '/home/media/media.lawrence.com/apps/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')

# URL that handles the static files like app media.
# Example: 'http://media.lawrence.com'
STATIC_URL = '/static/'

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]


#################################
# Config specifiche per il sito #
#################################

SITE_TITLE = "il_doc's"
ANALYTICS_ID = 'UA-7958919-14'
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
