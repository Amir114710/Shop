from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import  View , TemplateView , ListView , DetailView
from .models import Comments, Like, Product , Category

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
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        queryset = Product.objects.get(slug = self.object.slug)
        queryset.save()
        if self.request.user.is_authenticated == True:
            if self.request.user.likes.filter(products__english_title = self.object.english_title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context
    def post(self,request,slug):
        products = Product.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , products=products , user=request.user)
        return redirect('shop:shop_detail' , slug)

class Category_details(View):
    queryset = None
    template_name = 'shop/shop.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Category , id=pk)
        objects = queryset.products.all()
        category = Category.objects.all()
        return render (request , self.template_name , {'id':pk , 'products':objects , 'category':category})
    
def like(request , slug , pk):
    try:
        like = Like.objects.get(products__slug = slug , users_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(products_id=pk , users_id = request.user.id)
    return redirect('shop:shop_detail' , slug)
