from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with sample Listings"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Listing.objects.all().delete()

        for _ in range(20):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                price_per_night=round(random.uniform(50, 500), 2),
                location=fake.city(),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded listings'))
