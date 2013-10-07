# Std lib imports
# Django imports
from django.conf.urls import patterns, include, url

# 3rd party app imports
# local imports
from models import Article

urlpatterns = patterns('',
    url(r'^$', 
        'django.views.generic.list.ListView',
        {
            'queryset': Article.published.all(),
        },
        name='wiki_article_index'),
    url(r'^article/(?P<slug>[-\w]+)$', 
        'django.views.generic.detail.DetailView',
        {
            'queryset': Article.objects.all(),
        },
        name='wiki_article_detail'),
    url(r'^history/(?P<slug>[-\w]+)$', 'wiki.views.article_history', name='wiki_article_history'),
    url(r'^add/article$', 'wiki.views.add_article', name='wiki_article_add'),
    url(r'^edit/article/(?P<slug>[-\w]+)$', 'wiki.views.edit_article', name='wiki_article_edit'),
)