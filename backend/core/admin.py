from django.contrib import admin
from .models import ShopProduct, Order, ShopCategory

@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "category", "price", "compare_price", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "sku", "category"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "customer_name", "customer_email", "total", "status", "created_at"]
    list_filter = ["status", "payment_status"]
    search_fields = ["order_number", "customer_name", "customer_email"]

@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "products_count", "position", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "parent"]
