from django import forms
from django.forms import widgets
from .models import Employee

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'task']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'txtName'}),
             'email':forms.EmailInput(attrs={'class':'form-control', 'id':'txtEmailid'}),
              'task':forms.TextInput(attrs={'class':'form-control', 'id':'txtTask'}),


        }