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

try:
    from .local import *
except ImportError:
    pass
