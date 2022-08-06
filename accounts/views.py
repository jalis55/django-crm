import imp
from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customers=Customer.objects.all()
    orders=Customer.objects.all()
    context={'customers':customers,'orders':orders}
    print(context)
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products=Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customers(request):
    return render(request,'accounts/customer.html')
