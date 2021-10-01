from django.contrib import admin
from .models import Donations


class DonationsAdmin(admin.ModelAdmin):
    fields = (
        "name",
        'email',
        'amount',
    )
    readonly_fields = ('date',)


admin.site.register(Donations, DonationsAdmin)
