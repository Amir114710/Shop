from django.db import models

class Category(models.Model):
    image = models.FileField(upload_to='shop/category' , verbose_name="عکس دسته بندی")
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام دسته بندی")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "تنظیمات قسمت دسته بندی"

class Tags(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام برچسب")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = "تنظیمات قسمت  برچسب ها"



class Product(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام کالا")
    discription = models.TextField(null=True , blank=True , verbose_name="توضیحات کوتاه")
    price = models.SmallIntegerField(null=True , blank=True , verbose_name="قیمت کالا")
    code = models.SmallIntegerField(null=True , blank=True , verbose_name="کد کالا" , unique=True)
    category = models.ManyToManyField(Category , verbose_name="دسته بندی محصول")
    image = models.ImageField(upload_to='shop/products' , verbose_name="عکس کالا")
    tags = models.ManyToManyField(Tags , verbose_name="برچسب")
    status = models.BooleanField(default=True , verbose_name="ایا موجود است ؟")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = "تنظیمات قسمت محصولات"