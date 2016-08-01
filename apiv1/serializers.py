from rest_framework import serializers
from quotes.models import Quote
from blog.models import Post


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('text', 'author', 'url')


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('title', 'content_html', 'author', 'tags', 'pub_date', 'modified', 'get_absolute_url')
