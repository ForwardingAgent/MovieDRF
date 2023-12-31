"""
Django settings for bestfilmsdrf project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-0cc9*7x)%tj#+s&&r==7s&j-6&um3@v34#b%p5mh+^*ly^85*='
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'films',
    'rest_framework',
    'rest_framework.authtoken',  # из djoser Token Based Authentication
    'djoser',  # из djoser Token Based Authentication
    'drf_spectacular'  # документация

]

# При указании связующего программного обеспечения в списке MIDDLEWARE 
# из модуля settings.py необходимо соблюдать порядок СВЕРХУ ВНИЗ! 
# Порядок вызова Middleware важен для правильной работы приложений, уделяйте внимание соответствующим указаниям из документации библиотек Django, которые вы подключаете к своему проекту.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bestfilmsdrf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bestfilmsdrf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#       "default": {
#        "ENGINE": "django.db.backends.postgresql_psycopg2",
#        "NAME": os.environ.get('POSTGRES_DB'),
#        "USER": os.environ.get("POSTGRES_USER"),
#        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
#        "HOST": os.environ.get("DB_HOST"),
#        'PORT': 5432,
#        },
#    }

DATABASES = {
       "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
        }
        }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'madia')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # встроеный класс пагинации
    'PAGE_SIZE': 3,
    
    'DEFAULT_RENDERER_CLASSES' : [  # чтобы нельзя было править из строки браузера
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [  # эндпоинты только для авторизированых
    #     'rest_framework.permission.IsAuthenticated'
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [  # joser
        # 'rest_framework.authentication.TokenAuthentication',  # аунтефикация по token
        'rest_framework.authentication.BasicAuthentication',  # аунтефикация базовая от django по умолчанию
        # 'rest_framework.authentication.SessionAuthentication',  # аунтефикация по сессии, по умолчанию
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # документация
}

SPECTACULAR_SETTINGS = {  # 004 1.23 Marsh отдельные файлы urls и config в приложении api для  SPECTACULAR
    'TITLE': 'BestFilms',
    'DESCRIPTION': 'Best films with DRF',
    'VERSION': '1.0.0',
    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated'  # доступ толкько авторизованному
    ],
    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication'
    ],
    'SERVE_INCLUDE_SCHEMA': False,
}

#  добавить settings для Joser и JWT
# от Marsh 004