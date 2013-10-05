# Std lib imports
# Django imports
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# 3rd party app imports
# local imports
from admin import *

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^pastebin/', include('pastebin.urls')),

    # Examples:
    # url(r'^$', 'cdlibrary.views.home', name='home'),
    # url(r'^cdlibrary/', include('cdlibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
