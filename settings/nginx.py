from .base import *

ALLOWED_HOSTS = ['ildoc.it']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local_settings import *
except ImportError:
    pass
