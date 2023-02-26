from django.db import models

class objects_manager(models.Manager):
    def status(self):
        return self.filter(status=True)
class ContactUsModels(models.Model):
    username = models.CharField(max_length=200 , null=True , blank=True , verbose_name='نام')
    email = models.EmailField(null=True , blank=True , verbose_name='ایمیل کاربر')
    phone_number = models.IntegerField(null=True , blank=True , verbose_name='شماره تلفن کاربر')
    subject = models.CharField(max_length=1000 , null=True , blank=True , verbose_name=' موضوع ')
    message = models.TextField(null=True , blank=True , verbose_name=' پیام ')
    status = models.BooleanField(default=False , null=True , blank=True , verbose_name=' ایا چک شده است ؟ ')
    is_Accept_terms = models.BooleanField(default=False , verbose_name='پذیرفتن شرایط')
    objects = objects_manager()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'تماس با ما'
        verbose_name_plural = "تنظیمات قسمت تماس با ما" 

class Contacts(models.Model):
    address = models.CharField(max_length=1000 , null=True , blank=True , verbose_name='ادرس محل کار') 
    phone_number = models.BigIntegerField(null=True , blank=True , verbose_name='تلفن محل کار')
    email_address = models.EmailField(null=True , blank=True , verbose_name='ایمیل محل کار')
    facebook = models.CharField(max_length=10000 , null=True , blank=True , verbose_name='ادرس فیس بوک')
    twiter = models.CharField(max_length=10000 , null=True , blank=True , verbose_name='ادرس تویتر')
    linkdin = models.CharField(max_length=10000 , null=True , blank=True , verbose_name='ادرس لینک دین')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = "تنظیمات قسمت اطلاعات تماس" 
