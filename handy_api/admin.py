from django.contrib import admin
from .models import Address, HandyUser, Product, Cart, CartItem, Order, ProductImage
# Register your models here.

admin.site.register(Address)
admin.site.register(HandyUser)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
