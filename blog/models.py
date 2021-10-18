from django.db import models


class BlogPosts(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    story = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
