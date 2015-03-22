from django.conf.urls import patterns, url

from Articles import views

urlpatterns = patterns('',
    url('', views.index, name='index'),
)
