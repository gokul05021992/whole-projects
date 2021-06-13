from django.shortcuts import render
from . import models

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        models.web(name=name, email=email, message=message).save()
        return render(request, 'hoster/error.html')
    else:
        return render(request, 'hoster/index.html')