from django.conf import settings
from .models import Category, Post

def blog_common(request):
    categories = Category.objects.filter(pk__in = Post.objects.filter(status=Post.PUBLISHED).values('category')).order_by('title')
    return {
            'CATEGORIES': categories,
            }
