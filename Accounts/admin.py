
from django.contrib import admin
from .models import *
admin.site.register(NewUser)
search_fields = ['email']
autocomplete_fields = ['email', 'username', ]