from django.shortcuts import render
from.import models

def index(request):
    if request.method =="POST":
        name = request.POST['name']
        email= request.POST['name']
        message=request.POST['message']
        models.contact(name="name",email="email",message="message").save()
        return render(request,"dbconnectivity/submitted.html")
    else:
        return render(request,"dbconnectivity/index.html")
def sample(request):
    return render(request,'dbconnectivity/sample.html')
def login(request):
    if request.method =="POST":
        t=request.POST['username']
        m=request.POST['password']
        a='gokul'
        b='password'
        if t == a and m == b:
            return render(request,"dbconnectivity/hi.html")
            if request.method == "POST":
                firstname = request.POST['fname']
                lastname  = request.POST['lname']
                models.form(firstname="firstname",lastname="lastname").save()
                return render(requestcd,'dbconnectivity/submitted.html')
            else:
                return render(request,"dbconnectivity/hi.html")
        else:
            return render(request,"dbconnectivity/login.html")
    else:
        return render(request,"dbconnectivity/login.html")






# Create your views here.
