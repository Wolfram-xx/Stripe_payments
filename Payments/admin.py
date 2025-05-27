from django.contrib import admin
from Payments.models import *

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'order']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['tax', 'discount']

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'percent']

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'percent']
