# Generated by Django 3.1.5 on 2021-01-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='onSale',
            field=models.BooleanField(default=False),
        ),
    ]