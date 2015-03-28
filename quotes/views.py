from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Quote

def all_quotes(request):
    quote_list = Quote.objects.all().order_by('author')

    return render_to_response(
            'quotes/all_quotes.html',
            {
                'quote_list': quote_list,
            },
            context_instance=RequestContext(request)
        )
