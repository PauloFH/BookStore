# Generated by Django 5.1.1 on 2024-09-30 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_category_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
