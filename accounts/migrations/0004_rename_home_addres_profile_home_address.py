# Generated by Django 5.1.7 on 2025-03-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_home_addres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='home_addres',
            new_name='home_address',
        ),
    ]
