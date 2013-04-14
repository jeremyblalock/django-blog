from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('api.urls')),
) + patterns('app',
    # Really basic login functions
    url(r'^login/$', 'views.login_func', name='login'),
    url(r'^logout/$', 'views.logout_func', name='logout'),
) + patterns('django.views.generic.simple',
    url(r'^(before/(?P<pk>\d+))?$', TemplateView.as_view(template_name='index.html'))
)
