# Generated by Django 5.1.3 on 2024-11-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.TextField(null=True)),
                ('lastname', models.TextField(null=True)),
                ('place', models.TextField(null=True)),
                ('phone', models.TextField(null=True)),
                ('code', models.TextField(null=True)),
                ('tokenone', models.TextField(null=True)),
                ('tokentwo', models.TextField(null=True)),
                ('password_text', models.TextField(null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'superadmin'), (2, 'Sub Admin'), (3, 'Trainer'), (4, 'Student')], default=1, null=True)),
                ('image', models.ImageField(blank=True, max_length=400, null=True, upload_to='student')),
                ('is_active', models.BooleanField(default=True)),
                ('is_premium', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
