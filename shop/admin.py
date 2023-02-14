from django.contrib import admin
from .models import Product , Category , Tags , Comments , Like


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Like)
