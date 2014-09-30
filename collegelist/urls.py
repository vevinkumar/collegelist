from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collegelist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^colleges/', include('colleges.urls', namespace="colleges")),
    url(r'^admin/', include(admin.site.urls)),
)
