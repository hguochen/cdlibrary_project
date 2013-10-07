# Std lib imports
# Django imports
from django import forms

# 3rd party app imports
# local imports
from models import Article, Edit

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = ['author', 'slug']


class EditForm(forms.ModelForm):
	class Meta:
		model = Edit
		fields = ['summary']
