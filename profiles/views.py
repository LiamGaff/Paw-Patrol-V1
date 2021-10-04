from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from donation.models import Donations


@login_required
def profile(request):
    """ Return profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    donations = Donations.objects.filter(email=request.user.email)

    context = {
        'profile': profile,
        'donations': donations
    }
    return render(request, 'profiles/profiles.html', context)
