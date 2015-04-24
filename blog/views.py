from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required

from datetime import datetime

from .models import Post, Category, Tag
from .forms import PostForm


def index(request):
    post_list = Post.objects.filter(status=Post.PUBLISHED).prefetch_related('category').prefetch_related('tags').order_by('-pub_date')
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

    return render_to_response(
        'blog/index.html',
        {
            'latest_post_list': latest_post_list,
        },
        context_instance=RequestContext(request))


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(
            request,
            'blog/detail.html',
            {
                'post': post,
                'category': post.category,
            },
            context_instance=RequestContext(request)
        )


def category(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category, status=Post.PUBLISHED).select_related().order_by('-pub_date')
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

    return render_to_response(
            'blog/category.html',
            {
                'latest_post_list': latest_post_list,
                'category': category,
            },
            context_instance=RequestContext(request)
        )

def tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = Post.objects.filter(tags=tag, status=Post.PUBLISHED).select_related().order_by('-pub_date')
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

    return render_to_response(
            'blog/tag.html',
            {
                'latest_post_list': latest_post_list,
                'tag': tag,
            },
            context_instance=RequestContext(request)
        )

def taglist(request):
    tags = Tag.objects.filter(pk__in = Post.objects.filter(status=Post.PUBLISHED).values('tags')).order_by('title')
    return render_to_response(
            'blog/tags.html',
            {'tags': tags, },
            context_instance=RequestContext(request)
        )

'''
def author(request, slug)
    author = User.objects.get(slug=slug)
    post_list = Post.objects.filter(tags=tag).select_related().order_by('-pub_date')
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

    return render_to_response('tag.html', {
        'latest_post_list': latest_post_list,
        'tag': tag,
        },
        context_instance=RequestContext(request))
'''

def archives(request):
    post_list = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')

    return render_to_response(
            'blog/archives.html',
            {
                'post_list': post_list,
            },
            context_instance=RequestContext(request)
        )

@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render_to_response(
            'blog/post_add.html',
            {'form' : form },
            context_instance=RequestContext(request)
        )
