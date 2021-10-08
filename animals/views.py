from django.shortcuts import render
from home.models import Animal


def animals(request,):

    animals = Animal.objects.all()

    template = 'animals/animals.html'
    context = {
        'animals': animals,
    }
    return render(request, template, context)
