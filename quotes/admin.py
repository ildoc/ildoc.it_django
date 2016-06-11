from django.contrib import admin

from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Citazione', {'fields': ['text', 'author', 'url']})
    ]

    list_display = ('text', 'author', 'url')
    list_filter = ['author']
    search_fields = ['text', 'author']
    ordering = ['-created']

admin.site.register(Quote, QuoteAdmin)
