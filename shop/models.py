from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    fontasswoem = models.CharField(max_length=500 , null=True , blank=True , verbose_name="عکس دسته بندی")
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


class objects_manager(models.Manager):
    def status(self):
        return self.filter(status=True)
class Product(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام کالا")
    english_title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام اینگلیسی کالا")
    slug = models.SlugField(null=True , blank=True)
    discription = models.TextField(null=True , blank=True , verbose_name="توضیحات کوتاه")
    price = models.SmallIntegerField(null=True , blank=True , verbose_name="قیمت کالا")
    code = models.SmallIntegerField(null=True , blank=True , verbose_name="کد کالا" , unique=True)
    category = models.ManyToManyField(Category , verbose_name="دسته بندی محصول" , related_name="products")
    image = models.ImageField(upload_to='shop/products' , verbose_name="عکس کالا اصلی" , null=True , blank=True)
    image1 = models.ImageField(upload_to='shop/products' , verbose_name="1عکس کالا" , null=True , blank=True)
    image2 = models.ImageField(upload_to='shop/products' , verbose_name="2عکس کالا" , null=True , blank=True)
    image3 = models.ImageField(upload_to='shop/products' , verbose_name="3عکس کالا" , null=True , blank=True)
    tags = models.ManyToManyField(Tags , verbose_name="برچسب")
    content = models.TextField(null=True , blank=True , verbose_name='توضیحات بیشتر')
    tip1 = models.CharField(max_length=12000 , null=True , blank=True , verbose_name='نکته1')
    tip2 = models.CharField(max_length=12000 , null=True , blank=True , verbose_name='نکته2')
    tip3 = models.CharField(max_length=12000 , null=True , blank=True , verbose_name='نکته3')
    tip4 = models.CharField(max_length=12000 , null=True , blank=True , verbose_name='نکته4')
    tip5 = models.CharField(max_length=12000 , null=True , blank=True , verbose_name='نکته5')
    status = models.BooleanField(default=True , verbose_name="ایا موجود است ؟")
    special = models.BooleanField(default=False , verbose_name="ایا کالا ویژه است ؟")
    on_sale = models.BooleanField(default=False , verbose_name="ایا کالای حراج است ؟")
    objects = objects_manager()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = "تنظیمات قسمت محصولات"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Product , self).save(*args, **kwargs)