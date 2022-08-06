import imp
from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    
    total_customer=customers.count()
    total_orders=orders.count()
    total_pending=Order.objects.filter(status="Pending").count()
    total_delivered=Order.objects.filter(status="Delivered").count()
    context={
        'customers':customers,
        'orders':orders,
        'total_orders':total_orders,
        'total_customer':total_customer,
        'total_delivered':total_delivered,
        'total_pending':total_pending
        }
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products=Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customers(request):
    return render(request,'accounts/customer.html')
