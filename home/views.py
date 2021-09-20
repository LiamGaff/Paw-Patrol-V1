from django.shortcuts import render


def index(request):
    """ return index page """
    return render(request, 'home/index.html')
