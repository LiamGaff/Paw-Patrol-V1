from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import blogForm
from .models import BlogPost


def blog(request):
    """ return blog page """
    # posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    return render(request, template)


def blog_post(request):
    """ Add blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can add blog posts')
        return redirect(reverse('blog'))
    
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal has been added')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Unable to post blog. Please make sure you have filled in all the required fields.')
    else:
        form = blogForm()

    template = 'blog/blog_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
