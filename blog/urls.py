from django.conf.urls import patterns, url
from django.contrib.sitemaps.views import sitemap

from .sitemap import BlogSitemap, ViewSitemap
from .feeds import LatestEntriesFeed
from . import views

sitemaps = {
    "blog": BlogSitemap,
    #"view": ViewSitemap,
}

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    #url(r'^add/$', views.add_post, name='add_post'),

    url(r'^feeds/$', LatestEntriesFeed(), name='feeds'),

    url(r'^archives/$', views.archives, name='archives'),

    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name='tag'),
    url(r'^tags/$', views.taglist, name='taglist'),

    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),

    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
)
