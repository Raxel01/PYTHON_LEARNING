from django.shortcuts import render
from django.http import HttpResponse
from Thestore.models import Product
from django.db.models import Q 
# // what the fuck is that ??

def _say_Hello_(request):
    allProducts = Product.objects.filter(description__isnull=True)
    return render (request, 'hello.html', {'allProducts': allProducts})
# Create your views here.

def __Say_By__(request):
    return HttpResponse('Good By from SayBy view')

def _Presentation_(request):
    return HttpResponse('Hello here where I\'m presenting \
                        my self as a software devenopeen\
                        Yes this is right !')

# ana 3ayez anik