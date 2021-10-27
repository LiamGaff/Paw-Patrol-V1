import os
from django.shortcuts import render, redirect
from django.urls import reverse
from requests.exceptions import HTTPError
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import json
from django.http import HttpResponse, JsonResponse

from .forms import Amount


import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
publishableKey = os.environ.get('STRIPE_PUBLIC_KEY')


def donate(request):
    """ return doante page """
    form = Amount()

    context = {
        'form': form,
    }
    return render(request, "donation/donate.html", context)


@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        form = Amount(request.POST)
        if form.is_valid():
            amount = request.POST.get('amount', '')
            print(amount)

            customer = stripe.Customer.create(
                    name=request.user.get_username(),
                    email=request.user.email,
                    )

            intent = stripe.PaymentIntent.create(
                customer=customer,
                payment_method_types=['card'],
                amount=amount*100,
                currency=data['currency'],
            )
            return JsonResponse({'publishableKey': publishableKey,
                                'clientSecret': intent['client_secret']})


def successMsg(request):

    return render(request, "donation/success.html")


# Using Django
@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
