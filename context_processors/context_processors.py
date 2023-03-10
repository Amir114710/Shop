from account.models import User
from contactus.models import ContactUsModels, Contacts 
from shop.models import Category, Product
from django.core.paginator import Paginator


def category(request):
    category = Category.objects.all() 
    contact = Contacts.objects.all() 
    products = Product.objects.all()
    contactsus = ContactUsModels.objects.status()
    return {"category": category , 'contacts' : contact , 'products':products , 'contactsus':contactsus}
