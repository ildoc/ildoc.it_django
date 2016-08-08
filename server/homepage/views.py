from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from blog.models import Post, Tag


def index(request):
    post_list = Post.objects.filter(status=Post.PUBLISHED).prefetch_related('tags').order_by('-pub_date')
    paginator = Paginator(post_list, 10)

    page = request.GET.get('page')
    try:
        latest_post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_post_list = paginator.page(paginator.num_pages)

    return render(
        None,
        'homepage/index.html',
        {
            'latest_post_list': latest_post_list,
        },
        context_instance=RequestContext(request))
