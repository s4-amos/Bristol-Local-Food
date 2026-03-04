#!/usr/bin/env python
"""
Person A Sprint 1 Cleanup Script
Deletes all customer users (and their profiles) created during Sprint 1.
Use with caution!
Run with: docker-compose exec web python sprint1_personA_cleanup.py [--dry-run]
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bristol_food_network.settings')
django.setup()

from core.models import User

def cleanup(dry_run=False):
    customers = User.objects.filter(role='customer')
    count = customers.count()

    if count == 0:
        print("No customer users found. Nothing to clean.")
        return

    print(f"Found {count} customer user(s):")
    for user in customers:
        print(f"  - {user.email} ({user.first_name} {user.last_name})")

    if dry_run:
        print("\nDry run completed. No changes made.")
        return

    confirm = input(f"\nAre you sure you want to delete ALL {count} customer users and their profiles? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Cleanup cancelled.")
        return

    customers.delete()
    print(f"Deleted {count} customer users and their profiles.")

if __name__ == "__main__":
    dry_run = '--dry-run' in sys.argv
    cleanup(dry_run)