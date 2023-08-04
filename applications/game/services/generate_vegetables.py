
from faker import Faker
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)

def generate_vegetables(count=20):
    return [fake.vegetable() for _ in range(count)]
