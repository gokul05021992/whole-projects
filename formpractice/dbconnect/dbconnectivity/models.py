from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField()
    message = models.TextField(max_length=150)
class contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number =models.TextField()
class form(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)


