from django.contrib import admin

# Register your models here.
from .models import ghazals_home
from .models import famous_ghazals
from .models import new_ghazals

# Register your models here.

@admin.register(ghazals_home)
class ghazals_homeAdmin(admin.ModelAdmin):
    list_display = ['name', 'tags', 'writer','created', 'updated']

@admin.register(famous_ghazals)
class famous_ghazalsAdmin(admin.ModelAdmin):
    list_display = ['name', 'tags', 'writer','created', 'updated']

@admin.register(new_ghazals)
class new_ghazalsAdmin(admin.ModelAdmin):
    list_display = ['name', 'tags', 'writer','created', 'updated', 'verification_status']