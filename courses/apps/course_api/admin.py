from django.contrib import admin
from .models import course_info

"""
Registering the models here to publish them in the Django Admin Panel
"""
models = (course_info)
admin.site.register(models)
