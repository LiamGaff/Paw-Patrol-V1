from django.contrib import admin
from .models import Donations


class DonationsAdmin(admin.ModelAdmin):
    fields = (
        "name",
        'email',
        'date',
        'amount',
    )

    readonly_fields = (
        'date',
        'amount',
    )


admin.site.register(Donations, DonationsAdmin)
