from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Volunteer
from django.contrib import messages


def index(request):
    """ return index page """

    volunteers = Volunteer.objects.all()
    contact_form = ContactForm()

    template = 'home/index.html'
    context = {
        "volunteers": volunteers,
        'contact_form': contact_form
    }

    return render(request, template, context)


def messageForm(request):
    if request.method == "POST":
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'question': request.POST['question'],
        }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            query = contact_form.save()
            messages.success(request, 'Your question has been noted and someone will be in contact soon. Thankyou!')
            return redirect(reverse('home'))
    else:
        contact_form = ContactForm()
