# Generated by Django 4.2.20 on 2025-04-09 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orders_user_alter_reviews_user'),
        ('users', '0002_alter_user_options_alter_userroles_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
