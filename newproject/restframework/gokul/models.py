from django.db import models

class employeedetails(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=50)

