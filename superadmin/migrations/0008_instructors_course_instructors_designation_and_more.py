# Generated by Django 5.1.3 on 2024-11-16 18:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0007_remove_instructors_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructors',
            name='course',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='instructors',
            name='designation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instructor'),
        ),
    ]