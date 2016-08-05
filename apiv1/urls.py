from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^quotes/$', views.QuoteList.as_view()),
    url(r'^blog/$', views.PostList.as_view()),
    url(r'^add/$', views.PostCreate.as_view(), name='create'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.PostDetail.as_view(), name='detail'),
    url(r'^blog/(?P<slug>[\w-]+)/edit/$', views.PostUpdate.as_view(), name='update'),
    url(r'^blog/(?P<slug>[\w-]+)/delete/$', views.PostDelete.as_view(), name='delete'),
]
