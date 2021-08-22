from django.contrib import admin

# Register your models here.
from .models import ChildRegTable
from .models import ClientTable
admin.site.register(ChildRegTable)
admin.site.register(ClientTable)
