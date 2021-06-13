from django.db import models

class info(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.TextField()
    subject = models.TextField(max_length=100)


# Create your models here.
