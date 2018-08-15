import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&auwlm+_glkFEHAOSDIFJkhsdfoihjio#$@4gfasd3zx_m3!ov%75#pka'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'justforfun',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


