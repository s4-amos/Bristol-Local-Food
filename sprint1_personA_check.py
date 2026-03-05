#!/usr/bin/env python
"""
Person A Sprint 1 Database Verification
Checks only models created by Person A: User and CustomerProfile
Run with: docker-compose exec web python sprint1_personA_check.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bristol_food_network.settings')
django.setup()

from core.models import User
from customers.models import CustomerProfile

def check_person_a_sprint1():
    print("=" * 70)
    print("PERSON A - SPRINT 1 DATABASE VERIFICATION")
    print("(Models: User, CustomerProfile)")
    print("=" * 70)

    # ---- User model ----
    users = User.objects.all()
    print(f"\n👤 TOTAL USERS: {users.count()}")
    for u in users:
        print(f"\n  ── User: {u.email}")
        print(f"     Name: {u.first_name} {u.last_name}")
        print(f"     Role: {u.role}")
        print(f"     Address: {u.address or '(not provided)'}")
        print(f"     Postcode: {u.postcode or '(not provided)'}")

    # ---- CustomerProfile model ----
    profiles = CustomerProfile.objects.all()
    print(f"\n📦 TOTAL CUSTOMER PROFILES: {profiles.count()}")
    for cp in profiles:
        print(f"\n  ── Profile for: {cp.user.email}")
        print(f"     Phone: {cp.phone or '(not provided)'}")
        print(f"     Default delivery address: {cp.default_delivery_address or '(not provided)'}")

    # ---- Consistency check ----
    customer_users = User.objects.filter(role='customer')
    customers_without_profile = [
        u.email for u in customer_users
        if not hasattr(u, 'customer_profile')
    ]
    if customers_without_profile:
        print("\n⚠️  WARNING: Some customer users lack a CustomerProfile:")
        for email in customers_without_profile:
            print(f"     - {email}")
    else:
        print("\n✅ All customer users have a matching CustomerProfile.")

    print("\n" + "=" * 70)
    print("Person A Sprint 1 verification complete.")
    print("=" * 70)

if __name__ == "__main__":
    check_person_a_sprint1()