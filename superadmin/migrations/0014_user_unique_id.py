# Generated by Django 5.1.3 on 2024-11-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0013_rename_name_user_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unique_id',
            field=models.TextField(null=True, unique=True),
        ),
    ]
