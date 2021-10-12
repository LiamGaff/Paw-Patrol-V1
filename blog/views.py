from django.shortcuts import render


def blog(request):
    """ return blog page """
    return render(request, 'blog/blog.html')
