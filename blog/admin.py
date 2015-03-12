from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields':['title','content','category']}),
        ('Info', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('title','pub_date')
    list_filter = ['pub_date','modified_date']
    search_fields = ['title','content']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
