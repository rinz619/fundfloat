# Generated by Django 5.1.3 on 2024-11-16 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0006_instructors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructors',
            name='course',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='image',
        ),
    ]
