# Std lib imports
# Django imports
from django.conf.urls import patterns, include, url

# 3rd party app imports
# local imports
from models import Post
from views import index_view, add_post, view_post


urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^post/(?P<slug>[-\w]+)$', view_post, name='blog_post_detail'),
    url(r'^add/post/$', add_post, name='blog_add_post'),
    url(r'^archive/month/(?P<year>\d+)/(?P<month>\w+)$', 
    	'django.views.generic.dates.MonthArchiveView',
        {
            'queryset': Post.objects.all(), 
            'date_field': 'created_on',
        },
        name='blog_archive_month',
       ),
    url(r'^archive/week/(?P<year>\d+)/(?P<week>\d+)$',
        'django.views.generic.dates.WeekArchiveView',
        {
            'queryset': Post.objects.all(), 
            'date_field': 'created_on',
        },
        name='blog_archive_week',
       ),
)