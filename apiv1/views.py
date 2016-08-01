from django.shortcuts import render
from rest_framework import generics
from quotes.models import Quote
from blog.models import Post
from .serializers import QuoteSerializer, PostSerializer


class QuoteList(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostSerializer
