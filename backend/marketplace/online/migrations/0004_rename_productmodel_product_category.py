# Generated by Django 4.2.2 on 2023-06-25 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productmodel',
            new_name='category',
        ),
    ]
