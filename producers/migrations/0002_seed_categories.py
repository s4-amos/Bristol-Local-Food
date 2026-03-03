from django.db import migrations


CATEGORIES = [
    ('Vegetables', 'vegetables'),
    ('Fruit', 'fruit'),
    ('Dairy & Eggs', 'dairy-eggs'),
    ('Meat & Poultry', 'meat-poultry'),
    ('Bread & Bakery', 'bread-bakery'),
    ('Herbs & Spices', 'herbs-spices'),
    ('Honey & Preserves', 'honey-preserves'),
    ('Drinks & Juices', 'drinks-juices'),
    ('Grains & Pulses', 'grains-pulses'),
    ('Flowers & Plants', 'flowers-plants'),
]


def seed_categories(apps, schema_editor):
    Category = apps.get_model('producers', 'Category')
    for name, slug in CATEGORIES:
        Category.objects.get_or_create(slug=slug, defaults={'name': name})


def remove_categories(apps, schema_editor):
    Category = apps.get_model('producers', 'Category')
    Category.objects.filter(slug__in=[slug for _, slug in CATEGORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_categories, remove_categories),
    ]
