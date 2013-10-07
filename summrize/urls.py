from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^text/', include("text.urls", namespace="text")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    (r'^media/(.*)$','django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
)
