from django.db import models

# Create your models here.
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT)

    objects = models.Manager
