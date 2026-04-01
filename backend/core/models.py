from django.db import models

class ShopProduct(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=255, blank=True, default="")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    compare_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("draft", "Draft"), ("out_of_stock", "Out of Stock"), ("discontinued", "Discontinued")], default="active")
    weight = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255, blank=True, default="")
    customer_email = models.EmailField(blank=True, default="")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("processing", "Processing"), ("shipped", "Shipped"), ("delivered", "Delivered"), ("cancelled", "Cancelled"), ("returned", "Returned")], default="pending")
    payment_status = models.CharField(max_length=50, choices=[("paid", "Paid"), ("unpaid", "Unpaid"), ("refunded", "Refunded")], default="paid")
    order_date = models.DateField(null=True, blank=True)
    shipping_address = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.order_number

class ShopCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.CharField(max_length=255, blank=True, default="")
    products_count = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("hidden", "Hidden")], default="active")
    image_url = models.URLField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
