# Generated by Django 3.2.5 on 2021-08-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_order_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='furniture',
            old_name='furnitureDesc',
            new_name='furnitureGenres',
        ),
    ]
