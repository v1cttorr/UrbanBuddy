# Generated by Django 5.1.7 on 2025-03-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='home_addres',
            field=models.TextField(blank=True, default='Leżajsk, Mickiewicza 67', null=True),
        ),
    ]
