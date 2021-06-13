from django.db import models

class db(models.Model):
    name = models.TextField()
    email =models.EmailField()
    phone = models.CharField(max_length=100)
    message=models.CharField(max_length=100)
class form(models.Model):
    name = models.TextField()
    email =models.EmailField()
    phone = models.CharField(max_length=100)


# Create your models here.
