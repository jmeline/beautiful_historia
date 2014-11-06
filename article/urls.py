__author__ = 'jmeline'

from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns("",
                    ## Tutorial 4 Advanced urls/views
                    url(r'^all/$', views.articles),
                    url(r'^get/(?P<article_id>\d+)/$', views.article),
)

## Tutorial 3 urls/views
'''
url(r'^$', views.hello, name='hello'),
url(r'^hello_template/$', views.hello_template, name='hello_template'),
url(r'^hello_template_simple/$', views.hello_template_simple, name='hello_template_simple'),
url(r'^hello_class/$', HelloTemplate.as_view()),
'''

