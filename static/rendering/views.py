from django.http import HttpResponse
from django.shortcuts import render

def new(request):
    return HttpResponse("Good Mornignig")


def about(request):
    return render(request,'index.html')