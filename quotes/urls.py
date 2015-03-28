from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$',views.all_quotes, name='all_quotes'),
)
