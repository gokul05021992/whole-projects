from django.db import models

class web(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message= models.TextField(max_length=150)


# Create your models here.
