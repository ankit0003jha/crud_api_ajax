from django.http.response import JsonResponse
from crud_Api import models
from crud_Api.models import Employee
from django.shortcuts import render ,redirect
from rest_framework import generics
from .serializers import EmployeeSerializer
from crud_Api.forms import EmployeeRegistration
from rest_framework.decorators import (api_view, authentication_classes, permission_classes)

def index(request):  
    employees = Employee.objects.all() 
    form = EmployeeRegistration()
    return render(request,"index.html",{'employees':employees, 'form':form})

@api_view(["POST"])
def save(request):
    if request.method == "POST":
        form = EmployeeRegistration(request.POST)
        if form.is_valid():
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            task = request.POST['task']
            if id == "":
                usr = Employee(name = name, email=email, task=task)
            else:
                usr = Employee(id = id, name = name, email=email, task=task)
            usr.save()
            emp = Employee.objects.values()
            # print(emp)
            Employee_data = list(emp)
            return JsonResponse({'status':'Save', 'employee_data':Employee_data})
        else:
            return JsonResponse({'status':'Not Save'})


@api_view(["POST"])
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@api_view(["POST"])
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        em = Employee.objects.get(pk=id)
        em_data = {"id":em.id, "name":em.name, "email":em.email,
        "task":em.task}
        return JsonResponse(em_data)
    else:
        return JsonResponse({'status':0})




class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer