from django.shortcuts import render

def addition(request):
    return render(request,'servers/addition.html')
def add(request):
    gokul = float(request.GET["num1"])
    gokul1= float(request.GET["num2"])
    gs = gokul+gokul1
    return render(request,'servers/result.html',{"result":gs})


# Create your views here.
