from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name='tag'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name='category'),

    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
)
