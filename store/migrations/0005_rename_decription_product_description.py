# Generated by Django 5.0 on 2023-12-31 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]