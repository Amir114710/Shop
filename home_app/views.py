from django.shortcuts import render
from django.views.generic import TemplateView
from cart.cart_module import Cart
from contactus.models import ContactUsModels, Contacts
from home_app.models import Poster
from shop.models import Category


class TestView(TemplateView):
    template_name = "home_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactUsModels.objects.status()
        context['category'] = Category.objects.all()
        context['poster'] = Poster.objects.all()[:2]
        return context