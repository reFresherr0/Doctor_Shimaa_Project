# Generated by Django 5.1.2 on 2024-10-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0006_useractivitycategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created',
            new_name='publish_time',
        ),
        migrations.RenameField(
            model_name='useractivity',
            old_name='activity_timestamp',
            new_name='activity_time',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='article',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='content',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='feedback',
        ),
        migrations.AlterField(
            model_name='useractivitycategory',
            name='category_en',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
