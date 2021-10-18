from django.contrib import admin
from .models import BlogPosts


class BlogPostsAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'author',
        'story',
        'date'
        'image',
    )

    readonly_fields = (
        'date',
    )


admin.site.register(BlogPosts, BlogPostsAdmin)