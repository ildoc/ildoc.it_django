from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^quotes/$', views.QuoteList.as_view()),
    url(r'^blog/$', views.PostList.as_view()),
]
