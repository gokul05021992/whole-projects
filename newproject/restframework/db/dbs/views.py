from django.shortcuts import render
from django.contrib import messages
from. import models

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.contact(name=name,email=email,subject=subject,message=message).save()
        return render(request,'dbs/submitted.html')
    else:
        return render(request,'dbs/index.html')
def login(request):
    a="gokul"
    b="gokul"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        stud=models.contact.objects.all()
        if username == a and password == b:
            return render(request,'dbs/profile.html',{'key':stud})
        else:
            return render(request,'dbs/index.html')
    else:
        return render(request,"dbs/login.html")







# Create your views here.
