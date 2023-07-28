from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('cart/', views.cart, name='cart' ),
    path('checkout/', views.checkout, name='checkout' ),
    path('update_item/', views.updateItem, name='update-item'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.search, name = 'search'),
    path('category/<int:id>', views.category, name = 'category'),
    path('detail/<int:id>', views.detail, name = 'detail')
]