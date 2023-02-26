from django.urls import path
from . import views

app_name = 'pay'

urlpatterns = [
    path('<int:pk>' , views.PayDetail.as_view() , name='main_pay'),
    path('payed/<int:pk>' , views.PasyView.as_view() , name='payed'),
]

