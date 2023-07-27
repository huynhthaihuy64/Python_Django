from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pythonshop/home.html',context)
def cart(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer = customer, complete = False)
        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'pythonshop/cart.html',context)
def checkout(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer = customer, complete = False)
        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'pythonshop/checkout.html',context)
def updateItem(request):
   data = json.loads(request.body)
   productId = data['productId']
   action = data['action']
   customer = request.user.customer
   product = Product.objects.get(id = productId)
   order = Order.objects.filter(customer = customer, complete = False)
   if order.exists():
        order = order.first()
   else:
        order = Order.objects.create(customer=customer, complete=False)
   orderItem = OrderItem.objects.filter(order = order, product = product)
   if orderItem.exists():
        orderItem = orderItem.first()
   else:
        orderItem = OrderItem.objects.create(order = order, product = product)
   if action == 'add':
       orderItem.quantity += 1
   elif action == 'remove':
       orderItem.quantity -= 1
   orderItem.save()
   if orderItem.quantity <= 0:
       orderItem.delete()
   return JsonResponse('added',safe=False)