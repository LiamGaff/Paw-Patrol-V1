from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user', related_name='blogs')
    story = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-date"
        ]
