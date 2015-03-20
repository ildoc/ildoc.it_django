from django.conf import settings
from .models import Category

def blog_common(request):
    return {
            'CATEGORIES': Category.objects.all().order_by('title'),
            }
