from django.shortcuts import render
from.import models


def form(request):
    return render(request,'app/form.html')
def forms(request):
    if request.method == "POST":
        name = request.POST['firstname']
        lastname = request.POST['lastname']
        country = request.POST['country']
        subject = request.POST['subject']
        models.info(name=name,last_name=lastname,country=country,subject=subject).save()
        return render(request,"app/forms.html")
    else:
        return render(request,"app/form.html")






# Create your views here.
