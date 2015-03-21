__author__ = 'jmeline'
from django.contrib import admin

from django.conf.urls import patterns, url, include

from article import views

urlpatterns = patterns("",
                    ## Tutorial 4 Advanced urls/views
                    # url(r'^$', views.articles, name='home'),
                    url(r'^$', views.index, name='index'),
                    url(r'^about/', views.about, name='about'),
                    url(r'^get/(?P<article_id>\d+)/$', views.article, name='article'),
                    (r'^admin/', include(admin.site.urls)),



)

## Tutorial 3 urls/views
'''
url(r'^$', views.hello, name='hello'),
url(r'^hello_template/$', views.hello_template, name='hello_template'),
url(r'^hello_template_simple/$', views.hello_template_simple, name='hello_template_simple'),
url(r'^hello_class/$', HelloTemplate.as_view()),
'''

