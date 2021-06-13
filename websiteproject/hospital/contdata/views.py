from django.shortcuts import render
from.import models

def index(request):
    return render(request,'contdata/index.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        inquiry = request.POST['inquiry']
        message = request.POST['message']
        models.web(name=name,email=email,inquiry=inquiry, message=message).save()
        return render(request,'contdata/error.html')
    else:
        return render(request,'contdata/contact.html')
def about(request):
    return render(request,'contdata/about.html')
def videos(request):
    return render(request,'contdata/videoos.html')
def photos(request):
    return render(request,'contdata/photos.html')



