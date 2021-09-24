from django.shortcuts import render

def donate(request):
    """ return index page """


    return render(request, "donation/donate.html")