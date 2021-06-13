from django.shortcuts import render, redirect
from.login import contactform
from django.shortcuts import HttpResponse

def home(request):
    return render(request,"loginapp/home.html")
def signup(request):
    if request.method == "POST":
        gokul=contactform(request.POST)
        if gokul.is_valid():
            gokul.save()
            return redirect("home")
    else:
        gokul=contactform()
    return render(request,"loginapp/signup.html",{"fun":gokul})
def profile(request):
    return render(request,"loginapp/profile.html")
# Create your views here.
