from django.contrib import admin
from .models import Volunteer, Animal


class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
        "about",
        "image",
    )


class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'type',
        'breed',
        'about',
        "image",
    )


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Animal, AnimalAdmin)
