from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255 , default="unknown")
    subject = models.CharField(max_length=255 , null=True , blank= True )
    email = models.EmailField()
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["create_date"]

    def __str__(self):
        return f" {self.name}  >>> {self.message}"
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email