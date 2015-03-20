from django.conf import settings
from .models import Category

def blog_common(request):
    categories = Category.objects.all().order_by('title')
    return {
            'CATEGORIES': categories,
            }
