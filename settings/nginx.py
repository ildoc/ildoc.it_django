from .base import *

ALLOWED_HOSTS = ['ildoc.it']

try:
    from .local_settings import *
except ImportError:
    pass
