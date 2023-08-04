
from faker import Faker
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)

def generate_fruits(count=20):
    return [fake.fruit() for _ in range(count)]
