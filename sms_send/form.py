from django import forms
from .models import SmsSend



class SmsForm(forms.ModelForm):
    class Meta:
        model = SmsSend
        fields = '__all__'
