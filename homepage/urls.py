from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from .sitemap import BlogSitemap

from . import views

sitemaps = {
    "blog": BlogSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
