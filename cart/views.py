from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from shop.models import Product

class CartDetailView(TemplateView):
    template_name = 'includes/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'amir'
        return context

class CartAddView(View):
    def post(self , request , slug):
        product = get_object_or_404(Product , slug = slug)
        quntity = request.POST.get('quantity')
        return redirect(reverse('shop:main_shop'))

