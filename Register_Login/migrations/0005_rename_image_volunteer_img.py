# Generated by Django 5.1.2 on 2024-10-22 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0004_useractivitycategory_useractivity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='image',
            new_name='img',
        ),
    ]