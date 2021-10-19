from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'story',
        'date',
        'image',
        'id',
    )

    readonly_fields = (
        'date',
    )


admin.site.register(BlogPost, BlogPostAdmin)
