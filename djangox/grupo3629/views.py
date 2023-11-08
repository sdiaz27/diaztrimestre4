from django.http import HttpResponse
from django.shortcuts import render

# def home (request):
#     return HttpResponse('<h1>Hola Muendo Django ADSO')

def home (request):
    return render(request,'home.html')