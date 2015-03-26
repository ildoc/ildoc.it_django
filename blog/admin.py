from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    fieldsets = [
        ('Post', {'fields':['title', 'content', 'category', 'tags', 'status']})
    ]

    list_display = ('title', 'pub_date', 'modified_date', 'status')
    list_filter = ['pub_date', 'modified_date', 'status']
    search_fields = ['title', 'content']
    ordering = ['-pub_date']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['title']})
    ]
    list_display = ('title', 'slug')
    search_fields = ['title']

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tag', {'fields': ['title']})
    ]
    list_display = ('title', 'slug')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
