from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('' , views.ProductView.as_view() , name="main_shop"),
    path('detail/<slug:slug>' , views.ProductDetail.as_view() , name="shop_detail"),
    path('category/<int:pk>', views.Category_details.as_view() , name='category_detail'),
]