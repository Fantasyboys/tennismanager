from django.contrib import admin

from .models import Subject

# list of subject entities in admin part
admin.site.register(Subject)