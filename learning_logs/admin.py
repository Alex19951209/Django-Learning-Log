from django.contrib import admin

from .models import Topic, Entry

# Зарееструвати тут ваші моделі.
admin.site.register(Topic)
admin.site.register(Entry)