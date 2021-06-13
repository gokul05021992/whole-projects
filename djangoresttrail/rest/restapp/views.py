from django.shortcuts import render
from.models import employee
from django.http import request, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serialization import EmployeeSerializer

@csrf_exempt
@api_view(["GET"])
def Employeedetails(request):
    if request.method =="GET":
        print("list of employees :",dir(employee.objects))
        obj=employee.objects.all()
        return JsonResponse({"response":list(obj.values("id","name"))})
    else:
        if request.method =='POST':
            name=request.post['name']
            obj=employee(name=name)
            obj.save()
            data={"id":obj.id,"name":obj.name}
            return JsonResponse(data)
class Listemployee(APIView):
    def get(self, request):
        obj = employee.objects.all()
        # data = {"response": list(obj.values("id", "name"))}
        serializer_obj = EmployeeSerializer(obj, many=True)
        # return JsonResponse(data) # when APIView not used. but will work with APIView also
        return Response(serializer_obj.data)  # especially used when APIView is used.
        # status(http code), headers(can be used for auth), template_name(usually none), content_type(json/xml)
        # are the optional parameter of Response Object


    def post(self, request):
        # name = request.POST['name'] # this will not work if we use APIView wrapper and send post body as JSON
        # request.get('name') - to get query parameters of api request (will not work with APIView)
        # request.queryparams('name') - to get query parameter of api request if we use APIView

        # name = request.data['name']
        # obj = Employee(name=name)
        # obj.save()
        data = request.data
        serializer_obj = EmployeeSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)

        # data = {"response": {"id":obj.id, "name":obj.name}}
        # return JsonResponse(data) #work with both APIView and not APIView
        # return Response(data) # used when APIView is used
        return Response(serializer_obj.errors)


class UpdateEmployee(APIView):

    def get_Object(self, id):
        try:
            obj = employee.objects.get(id=id)
            return obj
        except employee.DoesNotExist:
            raise Http404

    def put(self, request, id):
        data = request.data
        # obj = Employee.objects.get(id=id)
        obj = self.get_Object(id)
        serializer_obj = EmployeeSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    def delete(self, request, id):
        # obj = Employee.objects.get(id = id)
        obj = self.get_Object(id)
        obj.delete()
        return Response({"response": "Employee is successfully deleted!"})

# Create your views here.
