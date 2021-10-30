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

    context = {
        'stripe_public_key': publishableKey
    }
    return render(request, "donation/donate.html", context)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        amount = request.POST.get('donate-value')
        
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'amount': int(amount)*100,
                    'quantity': 1,
                    'currency': 'eur',
                    'name': 'Donation'
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('paw-patrol-lg.herokuapp.com/donate/success/')),
            cancel_url=request.build_absolute_uri(reverse('paw-patrol-lg.herokuapp.com/'))
        )

        return redirect(session.url, code=303)


def success_msg(request):

    return render(request, "donation/success.html")


@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_3Uy1OKnA7JSh4YV7Xhr2KgPLSiPH3jEI'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)