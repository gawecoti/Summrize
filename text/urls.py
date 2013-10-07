from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.FeedView.as_view(), name="Feed"),
    url(r'^submit', views.TextAdd.as_view(), name="Submit"),
)
