from django.contrib import admin
from .models import Registration,OrderDetails,ItemsPrice
# Register your models here.
admin.site.register(Registration)
admin.site.register(OrderDetails)
admin.site.register(ItemsPrice)