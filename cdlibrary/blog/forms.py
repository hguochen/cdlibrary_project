# Std lib imports
# Django imports
from django import forms

# 3rd party app imports
# local imports
from models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['post']