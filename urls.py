from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^quotes/', include('quotes.urls', namespace='quotes')),

    #url(r'^snippets/', include('snippets.urls')),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include('blog.urls', namespace='blog')),

]
