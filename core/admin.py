from django.contrib import admin

# Register your models here.
from .models import BloodDonor, BloodReceiver

admin.site.register(BloodDonor)
admin.site.register(BloodReceiver)
