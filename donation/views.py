import os
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date
from requests.exceptions import HTTPError
from django.contrib import messages

from .models import Donations
from profiles.models import UserProfile

if os.path.exists("env.py"):
    import env

import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def donate(request):
    """ return doante page """

    return render(request, "donation/donate.html")


def charge(request):
    if request.method == 'POST':
        try:
            print('Data:', request.POST)

            amount = int(request.POST['donate-value'])

            customer = stripe.Customer.create(
                name=request.user.get_username(),
                email=request.user.email,
                source=request.POST['stripeToken']
                )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount*100,
                currency='eur',
                description="Donation"
            )

            donation = Donations(name=request.user.get_username(),
                                 email=request.user.email, amount=amount*100)
            donation.save()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            messages.error(request, 'An error occurred in processing your request. Please try again later.')
            return render(request, "donation/donate.html")

        except Exception as err:
            print(f'Other error occurred: {err}')
            messages.error(request, 'An error occurred in processing your request. Please try again later.')
            return render(request, "donation/donate.html")

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
      
    amount = args
    return render(request, "donation/success.html", {'amount': amount})
