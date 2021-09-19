from django.db import models
from django.db.models.fields import DateField


class Employee(models.Model):

    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    task = models.CharField(max_length=500)
    designation = models.CharField(max_length=70)
    joining_date = models.DateField(auto_now_add = True,blank=True, null=True)
    

    def __str__(self):
        return  f"{self.name}"