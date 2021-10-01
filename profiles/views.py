from django.shortcuts import render


def profile(request):
    """ Return profile page """

    return render(request, 'profiles/profile.html')
