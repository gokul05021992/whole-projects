from django.shortcuts import render
from django.http import request,JsonResponse
from.models import employeedetails

def employeedetails(request):
    if request.method == "GET":
        print("list of employee directory:" ,dir (employeedetails.objects))
        obj = employeedetails.objects.all()
        return JsonResponse({"response": list(obj.values("id","name"))})
    else:
        return render(request,"restpractice/templates")



# Create your views here.
