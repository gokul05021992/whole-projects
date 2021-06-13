from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    subject = models.TextField()
    message= models.TextField()

