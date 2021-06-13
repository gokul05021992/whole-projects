from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from.models import article
from.serializers import articleserialize

# Create your views here.

def artic(request):
    if request.method =='GET':
        articles=article.objects.all()
        serializer=articleserialize(articles,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        data =JSONParser().parse(request)
        serializer=articleserialize(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)



