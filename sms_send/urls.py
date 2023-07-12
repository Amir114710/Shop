from django.urls import path
from . import views


app_name = 'sms_send'


urlpatterns = [
    path('' , views.SmsView.as_view(), name='sms'),
]