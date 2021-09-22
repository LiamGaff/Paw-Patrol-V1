from django.shortcuts import render
from .models import Volunteer


def index(request):
    """ return index page """

    volunteers = Volunteer.objects.all()

    context = {
        "volunteers": volunteers
    }

    return render(request, 'home/index.html', context)
