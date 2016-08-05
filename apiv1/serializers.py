from rest_framework import serializers
from quotes.models import Quote
from blog.models import Post


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('text', 'author', 'url')


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('title', 'content_html', 'author', 'tags', 'pub_date', 'modified', 'get_absolute_url')


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('title', 'content_html', 'author', 'tags', 'pub_date', 'modified', 'get_absolute_url')


class PostCreateSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
