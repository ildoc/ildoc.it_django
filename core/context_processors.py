from django.conf import settings
from datetime import datetime
from dateutil.relativedelta import relativedelta


def core_values(request):
    data = {
        'SITENAME': getattr(settings, 'SITENAME', "il_doc's"),
        'ANALYTICS_ID': getattr(settings, 'ANALYTICS_ID', ''),
        'YEARS': relativedelta(datetime.today(), datetime(1990, 6, 22)).years
    }
    return data
