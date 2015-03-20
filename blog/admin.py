from django.contrib import admin

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields':['title', 'content', 'category', 'tags', 'status']}),
        ('Info', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('title', 'pub_date', 'modified_date', 'status')
    list_filter = ['pub_date', 'modified_date', 'status']
    search_fields = ['title', 'content']

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
