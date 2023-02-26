from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import View
from cart.models import Order
from pay.models import Pay
from django.urls import reverse_lazy

from shop.models import Notification

class PayDetail(View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        account = Pay.objects.all()
        return render(request , 'pay/pay.html' , {'order':order , 'account':account})

class PasyView(View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        account = Pay.objects.all()
        if request.FILES["image"]:
            image = request.FILES["image"]
        order.image_payed = image
        order.is_pay = True
        order.save()
        return redirect('home:main')
        
