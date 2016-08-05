from rest_framework import serializers
from django.template.defaultfilters import slugify
from quotes.models import Quote
from blog.models import Post, Tag


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('text', 'author', 'url')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class PostListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='apiv1:blog_detail',
        lookup_field='slug'
    )
    class Meta:
        model = Post
        fields = ('url', 'title', 'content_html', 'author', 'tags', 'pub_date', 'modified')

    def get_author(self, obj):
        return str(obj.author.username)


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='apiv1:blog_detail',
        lookup_field='slug'
    )
    class Meta:
        model = Post
        fields = ('url', 'title', 'content_html', 'author', 'tags', 'pub_date', 'modified')

    def get_author(self, obj):
        return str(obj.author.username)
        

class PostUpdateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.get(**validated_data)
        tag_list=[]
        for tag_data in tags_data:
            t, _ = Tag.objects.get_or_create(**tag_data)
            tag_list.append(t)
        post.tags = tag_list
        post.save()
        return post


class PostCreateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        tag_list=[]
        for tag_data in tags_data:
            t, _ = Tag.objects.get_or_create(**tag_data)
            tag_list.append(t)
        post.tags = tag_list
        post.save()
        return post
