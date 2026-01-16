from faker import Faker

fake = Faker()

print(fake.name())
print(fake.country())
print(fake.city())
print(fake.credit_card_number())