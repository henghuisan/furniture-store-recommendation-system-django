# Generated by Django 3.2.5 on 2021-09-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0029_auto_20210908_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='postcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]