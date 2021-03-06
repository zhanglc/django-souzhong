# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from magnet import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'search.views.home', name='home'),
                       # url(r'^search/', include('search.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^search/', ),
                       url(r'^$', views.index),
                       url(r'(?P<name>.+)/(?P<magnet_id>\d+)/$', views.magnet, name='magnet'),
)
