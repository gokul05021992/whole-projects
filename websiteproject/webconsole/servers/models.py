from django.db import models

class product(models.Model):
    name = models.TextField()
    price = models.TextField()
    count = models.TextField(default="0")
