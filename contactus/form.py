from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from account.models import User

class ContactForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام'}) , required=True)
    email = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'ایمیل'}) , required=True)
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)] , required=True)
    subject = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'موضوع'}) , required=True)
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control' , 'placeholder':'پیام'}) , required=True) 
    is_Accept_terms = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}) , required=True)
