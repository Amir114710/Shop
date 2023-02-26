from django.contrib import admin
from . import models

@admin.register(models.Pay)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number_of_cart' , 'owner_of_cart' , 'image')
