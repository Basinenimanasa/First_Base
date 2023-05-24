from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def firststring(request):
    return render(request,'Firstpage.html')
def secondstring(request):
    return HttpResponse('<marquee><h1>This is my first project</h1></marquee>')
    