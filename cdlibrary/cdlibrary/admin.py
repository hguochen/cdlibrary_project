# Std lib imports
# Django imports
from django.contrib import admin

# 3rd party app imports
# local imports
from models import Cd

admin.site.register(Cd)
admin.autodiscover()