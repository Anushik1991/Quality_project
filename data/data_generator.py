from faker import Faker
import random
import string


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_name(self):
        return self.fake.name()

    def generate_email(self):
        return self.fake.email()

    def generate_username(self):
        return self.fake.user_name() + str(random.randint(100, 999))

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))