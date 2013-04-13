from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('api.urls')),
) + patterns('app',
    url(r'^login/$', 'views.login_func', name='login'),
    url(r'^logout/$', 'views.logout_func', name='logout'),
)
