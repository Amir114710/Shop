from django.shortcuts import get_object_or_404, render
from django.views.generic import  View , TemplateView , ListView , DetailView
from .models import Product , Category

class ProductView(ListView):
    template_name = "shop/shop.html"
    model = Product
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class ProductDetail(DetailView):
    template_name = 'shop/single-product.html'
    model = Product
    context_object_name = 'products'

class Category_details(View):
    queryset = None
    template_name = 'shop/shop.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Category , id=pk)
        objects = queryset.products.all()
        category = Category.objects.all()
        return render (request , self.template_name , {'id':pk , 'products':objects , 'category':category})
