from django.db import models
from account.models import User


class SmsSend(models.Model):
    phone = models.CharField(max_length=11 ,null=True , blank=True ,verbose_name='کاربر')
    content = models.TextField(null=True , blank=True , verbose_name='توضیحات پیام')

    def __str__(self) -> str:
        return self.phone
    
    class Meta:
        verbose_name = "ارسال پیام"
        verbose_name_plural = "ارسال پیام به کاربر ها"