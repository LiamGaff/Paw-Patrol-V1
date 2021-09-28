import os
from django.shortcuts import render, redirect
from django.urls import reverse
from requests.exceptions import HTTPError
from django.http import JsonResponse
from django.contrib import messages

from .forms import SignupForm

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
                email=request.POST['email'],
                name=request.POST['name'],
                source=request.POST['stripeToken']
                )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount*100,
                currency='eur',
                description="Donation"
            )

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
    return render(request, "donation/success.html", {'amount':amount})


# def signUp(request):
#     if request.method == 'POST':
#         try:
#             if signup_form.is_valid():
#                 account = signup_form.save()
#                 messages.success(request, 'Your account has been created')
            
#         except:
#             contact_form = ContactForm()
#     else:
#         signup_form

