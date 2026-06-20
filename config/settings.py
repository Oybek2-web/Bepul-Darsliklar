from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-2v7jr5+(=f!f$10n8p6i!-pb8xgf%o6d_zu!+xyouaf_%v=*r*'

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "https://gown-judiciary-debating.ngrok-free.dev"
]

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',
    'rosetta',
    'accounts.apps.AccountConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'fanlar',
    'darslik',
    # 'accounts',
    'startup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.LogIPMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "darslik",
#         "USER": "postgres",
#         "PASSWORD": "12",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

# LOGIN_URL = 'accounts:login'
# LOGIN_REDIRECT_URL = 'fanlar:fanlar_list'
# LOGOUT_REDIRECT_URL = 'fanlar:fanlar_list'

LANGUAGE_CODE = 'en-us'
USE_I18N = True # i18n yoqildi
USE_L10N = True # l10n yoqildi
USE_TZ = True # Timezone


LANGUAGES = [
  ('en', _('English')),
  ('uz', _('O\'zbekcha')),
]

# Tarjima fayllari joylashuvi
LOCALE_PATHS = [
  BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'

# USE_I18N = True
#
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_ID = 1  # ← muhim!

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = 'accounts:login'
# LOGIN_REDIRECT_URL  = reverse_lazy('login')
# LOGOUT_REDIRECT_URL = reverse_lazy('logout')

LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/'

# Ixtiyoriy — email orqali login
ACCOUNT_LOGIN_METHODS      = {'email'}
ACCOUNT_EMAIL_REQUIRED     = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "oybekjon763@gmail.com"
EMAIL_HOST_PASSWORD = "odmhxuyiztgzxxda"
