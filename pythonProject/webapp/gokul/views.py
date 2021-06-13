from django.shortcuts import render
from. import models

def index(request):
    return render(request, 'gokul/index.html')

def contact(request):
    if request.method == 'POST':
        Email = request.POST['email']
        Subject = request.POST['subject']
        Message = request.POST['message']
        models.web(email=Email, subject=Subject, message=Message).save()
        return render(request, 'gokul/ERS.html')
    else:
        return render(request, 'gokul/contact.html')