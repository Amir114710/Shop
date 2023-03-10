from django.contrib import admin
from .models import Product , Category , Tags , Comments , Like , Notification , NotificationPersonal , AcceptTermsModel


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(NotificationPersonal)
admin.site.register(AcceptTermsModel)
