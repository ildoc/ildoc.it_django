from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from django.contrib.sitemaps.views import sitemap

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    url(r'^quotes/', include('quotes.urls', namespace='quotes')),

    url(r'^', include('blog.urls', namespace='blog')),
)
