from django.db import models

class Pay(models.Model):
    number_of_cart = models.CharField(max_length=16 , null=True , blank=True , verbose_name='شماره کارت')
    owner_of_cart = models.CharField(max_length=100 , null=True , blank=True , verbose_name='نام دارنده ی کارت')
    image = models.FileField(upload_to='pay/image', null=True , blank=True , verbose_name='عکس پرداخت موفق')

    def __str__(self) -> str:
        return self.owner_of_cart
    
    class Meta:
        verbose_name = "اطلاعات حساب برای پرداخت"
        verbose_name_plural = "تنظیمات قسمت اطلاعات حساب برای پرداخت ها"