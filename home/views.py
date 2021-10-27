import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Volunteer
from django.contrib import messages

from django.conf import settings


def index(request):
    """ return index page """

    volunteers = Volunteer.objects.all()
    contact_form = ContactForm()
    host = request.get_host()
    print(host)

    template = 'home/index.html'
    context = {
        "volunteers": volunteers,
        'contact_form': contact_form
    }

    return render(request, template, context)


def messageForm(request):
    """ Get from post data and email query to host_user """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email_host = os.environ.get('EMAIL_HOST_USER')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            question = request.POST.get('question', '')

            subject = "Contact form query"
            query = "\n".join([name, email, question])
            send_mail(subject, query, email_host,
                      ['liamgaffneytya@gmil.com'], fail_silently=False)
            messages.success(request, 
                             'Your question has been noted and someone will be in contact soon. Thankyou!')
            return redirect(reverse('home'))
    else:
        contact_form = ContactForm()
