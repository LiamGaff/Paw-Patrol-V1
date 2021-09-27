from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    fields = (
        "name",
        'email',
        'password',
    )

admin.site.register(Account, AccountAdmin)