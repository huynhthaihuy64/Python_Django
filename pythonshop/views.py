from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer = customer, complete = False)
        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'pythonshop/home.html',context)
def cart(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer = customer, complete = False)
        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'pythonshop/cart.html',context)
def checkout(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(customer = customer, complete = False)
        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'pythonshop/checkout.html',context)
def updateItem(request):
   data = json.loads(request.body)
   productId = data['productId']
   action = data['action']
   customer = request.user
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
def register(request):
    form = CreateUserForm()
    if request.method == "POST": 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'pythonshop/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'Login Failed')
    context = {}
    return render(request, 'pythonshop/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')