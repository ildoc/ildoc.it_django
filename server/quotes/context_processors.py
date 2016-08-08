import random

from django.conf import settings

from .models import Quote

def quotes_common(request):
    quotes_count = Quote.objects.count()
    randomquote = Quote()
    if quotes_count > 0:
        random_idx = random.randint(0, quotes_count - 1)
        randomquote = Quote.objects.all()[random_idx]
    else:
        randomquote.text = ''
        randomquote.author = ''
        randomquote.url = ''

    return {
            'RANDOMQUOTE': randomquote,
            }
