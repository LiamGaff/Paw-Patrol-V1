from django.db import models
import uuid


class Donations(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateField(auto_now_add=True)
    donation_id = models.CharField(max_length=32, null=False, editable=False)

    def _generate_donation_id(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.donation_id:
            self.donation_id = self._generate_donation_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
