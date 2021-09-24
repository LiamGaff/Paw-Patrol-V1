from django.shortcuts import render, redirect, reverse
from .models import Volunteer, ContactModel
from .forms import ContactForm

from django.contrib import messages
from django.views.generic.edit import FormView

def index(request):
    """ return index page """

    volunteers = Volunteer.objects.all()
    if request.method == "POST":
        form = ContactForm()
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Your quwstion has been noted and someone will be in contact soon. Thankyou!')
            return redirect(reverse('home'))
            
    else:
        contact_form = ContactForm()

    template = 'home/index.html'
    context = {
        "volunteers": volunteers, 
        'contact_form': contact_form,
    }

    return render(request, template, context)

        