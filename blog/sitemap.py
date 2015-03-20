from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import Post

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=Post.PUBLISHED)

    def lastmod(self, obj):
        return obj.modified_date

    # changefreq can be callable too
    def changefreq(self, obj):
        return "weekly"


class ViewSitemap(Sitemap):
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['index', 'taglist', 'archives']

    def location(self, item):
        return reverse(item)

    def changefreq(self, obj):
        return "daily"
