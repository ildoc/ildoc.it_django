from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from datetime import datetime

from .models import Post, Category, Tag


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

    return render_to_response('index.html', {
        'latest_post_list': latest_post_list,
        },
        context_instance=RequestContext(request))


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post': post},
    context_instance=RequestContext(request))


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

    return render_to_response('category.html', {
        'latest_post_list': latest_post_list,
        'category': category,
        },
        context_instance=RequestContext(request))

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

    return render_to_response('tag.html', {
        'latest_post_list': latest_post_list,
        'tag': tag,
        },
        context_instance=RequestContext(request))

def taglist(request):
    tags = Tag.objects.all().order_by('title')
    return render_to_response('tags.html', {'tags': tags, },
    context_instance=RequestContext(request))

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

    return render_to_response('archives.html', {
        'post_list': post_list,
        },
        context_instance=RequestContext(request))
