from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import blogForm
from .models import BlogPost


def blog(request):
    """ return blog page with posts and featured post"""
    posts = BlogPost.objects.all()
    recent_posts = BlogPost.objects.filter(published=True)[0:2]
    if BlogPost.objects.filter(id__gte=1):
        featured_post = posts[0]
    else:
        featured_post = None
    template = 'blog/blog.html'
    context = {
        'posts': posts,
        'featured_post': featured_post,
        'recent_posts': recent_posts,
    }
    return render(request, template, context)


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


def view_post(request, post_id):
    """ return blog page with posts and featured post"""
    post = get_object_or_404(BlogPost, pk=post_id)

    template = 'blog/blog_post.html'
    context = {
        'post': post
    }
    return render(request, template, context)
