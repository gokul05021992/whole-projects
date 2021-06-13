from django.shortcuts import render
from.models import student
from django.http import JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from.serialization import EmployeeSerializer

@csrf_exempt
@api_view(['GET','POST'])
def students(request):
    if request.method =="GET":
        obj=student.objects.all()
        data={"response":list(obj.values("id","name"))}
        return JsonResponse(data)
    elif request.method =="POST":
        name = request.POST['name']
        obj=student(name=name)
        obj.save()
        data={"id":obj.id,'name':obj.name}
        return JsonResponse(data)
class studentlist(APIView):
    def get(self,request):
        obj=student.objects.all()
        seri=EmployeeSerializer(obj,many=True)
        return Response(seri.data)
    def post(self,request):
        data=request.data
        seri=EmployeeSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors)
class editEmployee(APIView):
    def getObject(self,id):
        try:
            obj = student.objects.get(id)
            return obj
        except student.DoesnotExist:
            raise Http404
    def put(self,request,id):
        data= request.data
        obj=self.getObject(id)
        seri=EmployeeSerializer(obj,data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors)

    def delete(self,request,id):
        obj = self.getObject(id)
        obj.delete()
        return Response({"response":"Employee sucessfully deleted"})



















# Create your views here.
