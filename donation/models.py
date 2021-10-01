from django.db import models


class Donations(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
