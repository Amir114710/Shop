from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=100 , verbose_name='نام پوستر')
    content = models.TextField(null=True , blank=True , verbose_name='توضیحات پوستر')
    image = models.ImageField(upload_to='home/poster' , verbose_name="عکس پوستر " , null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'پوستر'
        verbose_name_plural = "تنظیمات قسمت پوستر"
