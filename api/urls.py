from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('api',
    url(r'^posts/$', views.PostList.as_view(), name='posts'),
    url(r'^posts/(?P<pk>\d+)$', views.PostItem.as_view()),
)
