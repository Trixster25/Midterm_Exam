import random
from faker import Faker
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()

def generate_transaction_id(length=10):
    """Generate a random alphanumeric transaction ID."""
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

# Generate 10 fake transaction records
transaction_records = []
for _ in range(10):
    transaction = {
        "transaction_id": generate_transaction_id(),
        "transaction_date": fake.date_this_year(),
        "amount": round(random.uniform(100.00, 5000.00), 2)
    }
    transaction_records.append(transaction)

# Print each transaction in a readable format
for i, record in enumerate(transaction_records, start=1):
    print(f"Transaction {i}:")
    print(f"  Transaction ID: {record['transaction_id']}")
    print(f"  Transaction Date: {record['transaction_date']}")
    print(f"  Amount: ${record['amount']}")
    print()
