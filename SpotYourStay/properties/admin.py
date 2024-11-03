from django.contrib import admin

# Register your models here.

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=('name', 'owner')