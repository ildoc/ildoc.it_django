from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    fieldsets = [
        ('Post', {'fields': ['title', 'content', 'tags', 'status']})
    ]

    list_display = ('title', 'pub_date', 'modified', 'status')
    list_filter = ['pub_date', 'modified', 'status']
    search_fields = ['title', 'content']
    ordering = ['-pub_date']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tag', {'fields': ['title']})
    ]
    list_display = ('title', 'slug')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
