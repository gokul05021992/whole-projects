from django.shortcuts import render
from.import models
from.forms import contactform

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message=request.POST['message']
        models.db(name=name,email=email,phone=phone,message=message).save()
        return render(request,"service/error.html")
    else:
        return render(request,"service/index.html")

def former(request):
    gokul=contactform()
    return render(request,"service/former.html",{'form':gokul})
def submitted(request):
    if request.method == "POST":
        name = request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        models.form(name=name,email=email,phone=phone).save()
        return render(request,"service/submitted.html")
    else:
        return render(request,"service/index.html")

