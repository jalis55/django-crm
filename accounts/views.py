from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm
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

def customers(request,cust_id):
    customer=Customer.objects.get(id=cust_id)
    orders=customer.order_set.all()
    total_order=orders.count()

    context={
        'customer':customer,
        'orders':orders,
        'total_order':total_order
        }
    return render(request,'accounts/customer.html',context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)