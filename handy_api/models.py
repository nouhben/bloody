from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
import uuid


class Address(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    zipCode = models.CharField(max_length=10, null=True, blank=True)
    flat = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.country}, flat {self.city}, zipcode {self.zipcode}'


class HandyUser(models.Model):
    base = models.OneToOneField(User, models.CASCADE)
    address = models.OneToOneField(
        Address, models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        default='users_images/default.png', upload_to='users_images',
        null=True,
    )
    # extends the parent save to add functionality
    # we want to scale down the images uploaded by the users

    def __str__(self) -> str:
        return f'{self.base.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ProductImage(models.Model):
    def __str__(self) -> str:
        return f'{self.image.name}'
    image = models.ImageField(
        default='products_images/default.png',
        upload_to='products_images',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    availableQuantity = models.IntegerField(default=1)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Cart {self.user}'

    @property
    def total(self):
        return sum([item.total for item in self.items])

    @property
    def items(self):
        items = self.cartitem_set.all()
        return items


class CartItem(models.Model):
    product = models.OneToOneField(Product, models.CASCADE)
    # product = models.OneToOneField(Cart, models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.quantity * self.product.price


class Order(models.Model):
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
        ('Delivered', 'Delivered'),
        ('Shipped', 'Shipped'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
    )
    total = models.SmallIntegerField(default=0)

    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=30, choices=ORDER_STATUS)
    transaction_id = models. CharField(max_length=100, null=True)

    @property
    def items(self):
        return self.cart.items
