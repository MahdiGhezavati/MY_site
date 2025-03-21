from django.db import models

# Create your models here.

class Post(models.Model):
    # author 
    # image
    # tag
    # category
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


