from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('' , views.CartDetailView.as_view() , name='cart_main'),
    path('add/<slug:slug>' , views.CartAddView.as_view() , name='cart_add'),
]