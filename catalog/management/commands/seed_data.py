from catalog.seeders.products import seed_products
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        product_count = seed_products()

        self.stdout.write(
            self.style.SUCCESS(
                f"✅ {product_count} Products Created."
            )
        )
    