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
        # print("HERE")
        data = json.loads(request.body)
        amount = 10
        value = request.POST.get('amount', '')
        if value is None:
            print(value)
        else:
            print("Value: "+value)

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


def success_msg(request):

    return render(request, "donation/success.html")