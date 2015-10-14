from django.conf import settings
from datetime import datetime
from dateutil.relativedelta import relativedelta

def global_settings(request):
    return {
            'SITENAME': settings.SITENAME,
            'YEARS': relativedelta(datetime.today(), datetime(1990, 6, 22)).years
            }
