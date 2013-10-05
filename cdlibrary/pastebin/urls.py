# Std lib imports
# Django imports
from django.conf.urls import patterns, url

# 3rd party app imports
# local imports
from models import Paste
from views import PasteView, PasteDetailView

urlpatterns = patterns('',
	url(r'^$', PasteView.as_view()),
	url(r'^paste/(?P<object_id>\d+)$', PasteDetailView.as_view(), name='pastebin_paste_detail'),
)