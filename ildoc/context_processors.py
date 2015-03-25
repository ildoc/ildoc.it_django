from django.conf import settings

def global_settings(request):
    return {
            'VERSION': settings.VERSION,
            'SITENAME': settings.SITENAME,
            'GOOGLE_ANALYTICS' : settings.GOOGLE_ANALYTICS,
            }
