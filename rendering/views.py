from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def new(request):
    return HttpResponse("Good Mornignig")


def home(request):
   


    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

 
    return render(request,'index.html',context)