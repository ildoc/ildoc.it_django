from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Post

class LatestEntriesFeed(Feed):
    title = "il_doc's"
    link = "/"
    description = "Feed dei post"

    def items(self):
        return Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html
