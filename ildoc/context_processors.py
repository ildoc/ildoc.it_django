from datetime import datetime

from django.conf import settings

def global_settings(request):
    return {
            'SITENAME': settings.SITENAME,
            }
