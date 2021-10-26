from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from home.models import Animal
from .forms import addAnimalForm


def animals(request):
    """ DIsplay animals from database
        and render animals page """
    animals = Animal.objects.all()

    template = 'animals/animals.html'
    context = {
        'animals': animals,
    }
    return render(request, template, context)


@login_required
def add_animal(request):
    """ Add animals to the data base """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can make this change.')
        return redirect(reverse('animals'))
    
    if request.method == 'POST':
        form = addAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save()
            messages.success(request, 'Animal has been added')
            return redirect(reverse('animals'))
        else:
            messages.error(request, 'Unable to add animal. Please make sure you have filled in all the required fields.')
    else:
        form = addAnimalForm()

    template = 'animals/add_animal.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_animal(request, animal_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can make this change.')
        return redirect(reverse('animals'))
    
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.delete()
    messages.success(request, 'Animal has been removed')
    return redirect(reverse('animals'))


@login_required
def edit_animal(request, animal_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can make this change.')
        return redirect(reverse('animals'))

    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = addAnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal has been updated!')
            return redirect(reverse('animals'))
        else:
            messages.error(request, 'Unable to update animal. Please make sure you have filled in all the required fields.')
    else:
        form = addAnimalForm(instance=animal)
        messages.info(request, f'You are editing {animal.name}')

    template = 'animals/edit_animal.html'
    context = {
        'form': form,
        'animal': animal,
    }

    return render(request, template, context)
