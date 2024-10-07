from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a list of 10 user profiles
user_profiles = []
for _ in range(10):
    profile = {
        "full_name": fake.name(),
        "email": fake.email(),
        "job_title": fake.job(),
        "company": fake.company()
    }
    user_profiles.append(profile)

# Print each profile in a structured format
for i, profile in enumerate(user_profiles, start=1):
    print(f"Profile {i}:")
    print(f"  Full Name: {profile['full_name']}")
    print(f"  Email: {profile['email']}")
    print(f"  Job Title: {profile['job_title']}")
    print(f"  Company: {profile['company']}")
    print()
