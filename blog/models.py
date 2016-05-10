from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title