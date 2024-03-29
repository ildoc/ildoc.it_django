from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.template.defaultfilters import slugify

from .models import Post, Tag
from .forms import PostForm


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
        'blog/post_list.html',
        {
            'latest_post_list': latest_post_list,
            'nbar': 'blog',
        },
        context_instance=RequestContext(request))


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.status==Post.DRAFT and not request.user.is_superuser:
        raise PermissionDenied

    return render(
        request,
        'blog/detail.html',
        {
            'post': post,
            'nbar': 'blog',
        },
        context_instance=RequestContext(request)
    )


def tag(request, slug):
    try:
        tag = Tag.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

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
            'nbar': 'blog',
        },
        context_instance=RequestContext(request)
    )


def taglist(request):
    tags = Tag.objects.filter(pk__in=Post.objects.filter(status=Post.PUBLISHED).values('tags')).order_by('title')
    return render_to_response(
        'blog/tags.html',
        {
            'tags': tags,
            'nbar': 'blog',
        },
        context_instance=RequestContext(request)
    )


def archives(request):
    post_list = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')

    return render_to_response(
        'blog/archives.html',
        {
            'post_list': post_list,
            'nbar': 'blog',
        },
        context_instance=RequestContext(request)
    )


@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':

        print(request.POST)
        tags = request.POST.getlist('tags')
        tags_added = []
        for tag in tags:
            t, created = Tag.objects.get_or_create(title=tag)
            if created:
                tags_added.append(tag)
        request.POST.setlist('tags', Tag.objects.filter(slug__in=[slugify(tag) in tags]))

        form = PostForm(data=request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.save()
            form.save_m2m()
            return HttpResponseRedirect("/")
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render_to_response(
        'blog/post_add.html',
        {
            'form': form,
            'nbar': 'blog',
        },
        context_instance=RequestContext(request)
    )
