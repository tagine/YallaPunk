from .base import *

from yallapunk.config import config_loader

config = config_loader('production')

DEBUG = False

SECRET_KEY = config['SECRET_KEY']

ALLOWED_HOSTS = config['ALLOWED_HOSTS']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

db = config['DB']

DATABASES = {
    'default': {
        'NAME': db['NAME'],
        'ENGINE': db['ENGINE'],
        'HOST': db['HOST'],
        'PORT': db['PORT'],
        'USER': db['USER'],
        'PASSWORD': db['PASSWORD'],
    }
}

INSTALLED_APPS.extend([
    'django_s3_storage',
])

# django_s3_settings
STATIC_S3_BUCKET = config['S3']['STATIC']
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = STATIC_S3_BUCKET
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % STATIC_S3_BUCKET
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

try:
    from .local import *
except ImportError:
    pass
