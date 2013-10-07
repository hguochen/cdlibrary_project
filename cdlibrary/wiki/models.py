# Std lib imports
# Django imports
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# 3rd party app imports
# local imports


class PublishedArticlesManager(models.Manager):

	def get_query_set(self):
		return super(PublishedArticlesManager, self).get_query_set().filter(is_published=True)


class Article(models.Model):
	"""Represents a wiki article"""

	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50, unique=True)
	text = models.TextField(help_text="Formatted using ReST")
	author = models.ForeignKey(User)
	is_published = models.BooleanField(default=False, verbose_name="Publish?")
	created_on = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()
	published = PublishedArticlesManager()

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('wiki_article_detail', (), {'slug': self.slug})


class Edit(models.Model):
	"""Stores an edit session"""

	article = models.ForeignKey(Article)
	editor = models.ForeignKey(User)
	edited_on = models.DateTimeField(auto_now_add=True)
	summary = models.CharField(max_length=100)

	class Meta:
		ordering = ['-edited_on']

	def __unicode__(self):
		return "%s - %s - %s" % (self.summary, self.editor, self.edited_on)

	@models.permalink
	def get_absolute_url(self):
		return ('wiki_edit_detail', self.id)