from rest_framework import generics

from quotes.models import Quote
from blog.models import Post

from .serializers import QuoteSerializer, PostListSerializer, PostDetailSerializer, PostCreateSerializer


class QuoteList(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreate(generics.CreateAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostCreateSerializer


class PostUpdate(generics.UpdateAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDelete(generics.DestroyAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
