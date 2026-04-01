from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import ShopProduct, Order, ShopCategory
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusCommerce with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuscommerce.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if ShopProduct.objects.count() == 0:
            for i in range(10):
                ShopProduct.objects.create(
                    name=f"Sample ShopProduct {i+1}",
                    sku=f"Sample {i+1}",
                    category=f"Sample {i+1}",
                    price=round(random.uniform(1000, 50000), 2),
                    compare_price=round(random.uniform(1000, 50000), 2),
                    stock=random.randint(1, 100),
                    status=random.choice(["active", "draft", "out_of_stock", "discontinued"]),
                    weight=round(random.uniform(1000, 50000), 2),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ShopProduct records created'))

        if Order.objects.count() == 0:
            for i in range(10):
                Order.objects.create(
                    order_number=f"Sample {i+1}",
                    customer_name=f"Sample Order {i+1}",
                    customer_email=f"demo{i+1}@example.com",
                    total=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["pending", "processing", "shipped", "delivered", "cancelled", "returned"]),
                    payment_status=random.choice(["paid", "unpaid", "refunded"]),
                    order_date=date.today() - timedelta(days=random.randint(0, 90)),
                    shipping_address=f"Sample shipping address for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Order records created'))

        if ShopCategory.objects.count() == 0:
            for i in range(10):
                ShopCategory.objects.create(
                    name=f"Sample ShopCategory {i+1}",
                    parent=f"Sample {i+1}",
                    products_count=random.randint(1, 100),
                    position=random.randint(1, 100),
                    status=random.choice(["active", "hidden"]),
                    image_url=f"https://example.com/{i+1}",
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 ShopCategory records created'))
