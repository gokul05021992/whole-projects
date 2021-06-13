from django.shortcuts import HttpResponse

def sample(request):
    return HttpResponse("<a href="https://www.w3schools.com">Visit W3Schools</a>")
