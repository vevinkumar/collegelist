from django.conf.urls import patterns, url

from colleges import views

urlpatterns = patterns('',
	# ex: /colleges/
    url(r'^$', views.index, name='index'),
	# ex: /colleges/districts/
    url(r'^districts/$', views.districts, name='districts'),
    # ex: /colleges/logmeout/
    url(r'^logmeout/$', views.logmeout, name='logmeout'),
    # ex: /colleges/districts/chennai/
    #url(r'^districts/(?P<district>\w+)/$', views.CollegesView.as_view(), name='colleges'),
    url(r'^districts/(?P<district>\w+)/$', views.colleges, name='colleges'),
    # ex: /colleges/5/
    url(r'^(?P<college_id>\d+)/$', views.details, name='details'),
	# ex: /colleges/validate/
	#url(r'^validate/$', views.validate, name='validate'),

)