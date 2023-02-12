from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('' , views.TestView.as_view() , name="main_shop")
]