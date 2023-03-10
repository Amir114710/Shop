from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from shop.models import Product



class AboutModel(models.Model):
    about_shop = RichTextUploadingField(null=True , blank=True , verbose_name="درباره فروشگاه")
    image1 = models.FileField(upload_to='about/image' , null=True , blank=True , verbose_name="عکس 1 فروشگاه")
    image2 = models.FileField(upload_to='about/image' , null=True , blank=True , verbose_name="عکس 2 فروشگاه")
    image3 = models.FileField(upload_to='about/image' , null=True , blank=True , verbose_name="عکس 3 فروشگاه")

    def __str__(self) -> str:
        return self.about_shop
    
    class Meta:
        verbose_name = 'درباره فروشگاه'
        verbose_name_plural = "تنظیمات درباره ی فروشگاه"

class PosterAbout(models.Model):
    products = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='posters' , verbose_name='انتخاب کالا')
    content = RichTextUploadingField(null=True , blank=True , verbose_name="درباره پوستر")

    def __str__(self) -> str:
        return self.products.title
        
    class Meta:
        verbose_name = 'پوستر'
        verbose_name_plural = "تنظیمات پوستر درباره ما "

class PropertyShop(models.Model):
    fontasswoem = models.CharField(max_length=500 , null=True , blank=True , verbose_name="عکس بصورت فونت اسم(توضیح داده شده.)")
    title = models.CharField(max_length=500 , null=True , blank=True , verbose_name="اسم ویژگی")
    content = models.TextField(max_length=500 , null=True , blank=True , verbose_name="توضیحاتی درباره ی ویژگی")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'ویژگی ها'
        verbose_name_plural = "تنظیمات  ویژگی ها "   
