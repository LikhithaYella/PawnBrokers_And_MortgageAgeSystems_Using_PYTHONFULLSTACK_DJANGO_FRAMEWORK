# Generated by Django 4.1.7 on 2023-03-31 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_signup_registration_alter_registration_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration',
            new_name='RegistrationForm',
        ),
    ]
