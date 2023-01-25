from django.contrib import admin  # noqa: F401

from .models import Choice, Question

admin.site.register([Question, Choice])
