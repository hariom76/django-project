from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.func),
    path('login/',views.login),
    path('login1/',views.login1),
    path('order/',views.order),
    path('itemspage/',views.itemspage),
    path('payment/',views.payment),
    path('order1/',views.order1),
]