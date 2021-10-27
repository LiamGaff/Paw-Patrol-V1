from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    fields = (
        "name",
        'email',
        'date',
        'amount',
        'donation_id'
    )

    readonly_fields = (
        'date',
        'amount',
        'donation_id'
    )


admin.site.register(Donation, DonationAdmin)
