from django.core.management.base import BaseCommand
from products.models import Category, Product
import requests

class Command(BaseCommand):
    help = "Seed 100 products into the database from DummyJSON API"

    def handle(self, *args, **kwargs):
        url = "https://dummyjson.com/products?limit=100"
        response = requests.get(url)
        data = response.json()

        Product.objects.all().delete()  # clear old products

        for item in data["products"]:
            category, _ = Category.objects.get_or_create(name=item["category"])
            Product.objects.create(
                name=item["title"],
                description=item["description"],
                price=item["price"],
                image_url=item["thumbnail"],  # DummyJSON uses 'thumbnail'
                category=category,
            )

        self.stdout.write(self.style.SUCCESS("100 products seeded successfully!"))
