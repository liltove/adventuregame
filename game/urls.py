from django.conf.urls import patterns, include, url

from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
