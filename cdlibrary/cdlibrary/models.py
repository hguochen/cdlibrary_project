# Std lib imports
# Django imports
from django.db import models

# 3rd party app imports
# local imports

GENRE_CHOICES = (('R', 'Rock'),
				 ('B', 'Blues'),
				 ('J', 'Jazz'),
				 ('P', 'Pop'))

class Cd(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	artist = models.CharField(max_length=40)
	date = models.DateField()
	genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

	def __unicode__(self):
		"""
		The __unicode__ property of the model defines it's string representation which 
		will be used in the admin interface, shell etc.
		"""

		return "%s by %s, %s-%s-%s" % (self.title,
								 self.artist,
								 self.date.year, 
								 self.date.month, 
								 self.date.day)
