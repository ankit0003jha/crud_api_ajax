from django.db import models
from django.db.models.fields import DateField


class Employee(models.Model):

    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    task = models.CharField(max_length=500)
    

    def __str__(self):
        return  f"{self.name}"
