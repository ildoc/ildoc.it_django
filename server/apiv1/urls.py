from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    url(r'^auth/token/', obtain_jwt_token),
    url(r'^quotes/$', views.QuoteList.as_view()),
    url(r'^blog/$', views.PostList.as_view()),
    url(r'^add/$', views.PostCreate.as_view(), name='blog_create'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.PostDetail.as_view(), name='blog_detail'),
    url(r'^blog/(?P<slug>[\w-]+)/edit/$', views.PostUpdate.as_view(), name='blog_update'),
    url(r'^blog/(?P<slug>[\w-]+)/delete/$', views.PostDelete.as_view(), name='blog_delete'),
]
