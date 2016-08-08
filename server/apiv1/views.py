from rest_framework import generics
from rest_framework import permissions

from quotes.models import Quote
from blog.models import Post

from .serializers import QuoteSerializer, PostListSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer
from .permissions import IsOwnerOrReadOnly


class QuoteList(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date').prefetch_related('tags')
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date').prefetch_related('tags')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreate(generics.CreateAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdate(generics.RetrieveUpdateAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly]
    lookup_field = 'slug'


class PostDelete(generics.DestroyAPIView):
    queryset =  Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwnerOrReadOnly]
    lookup_field = 'slug'
