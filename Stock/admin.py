from django.contrib import admin
from .models import Inventory,User_stock,All_Stock
# Register your models
admin.site.register(Inventory) 
admin.site.register(All_Stock) 
admin.site.register(User_stock) 