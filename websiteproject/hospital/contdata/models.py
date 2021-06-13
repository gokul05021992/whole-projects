from django.db import models

class web(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    inquiry = models.CharField(max_length=50)
    message = models.TextField(max_length=150)



