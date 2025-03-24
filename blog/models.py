from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.SET_NULL,null=True)
    image  = models.ImageField(upload_to="media/blog" , default="media/blog/default.jpg")
    # tag
    category = models.ManyToManyField(category)
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_view = models.IntegerField(default = 1)
    status = models.BooleanField(default=False)
    poblished_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_date"]
 
    def __str__(self):
        return f" {self.id} - {self.title} "
