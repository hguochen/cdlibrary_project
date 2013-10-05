# Std lib imports
# Django imports
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# 3rd party app imports
# local imports
from models import Paste


class PasteView(CreateView):
	model = Paste
	fields = ['text', 'name']	

class PasteDetailView(DetailView):
	model = Paste
	queryset = Paste.objects.all()