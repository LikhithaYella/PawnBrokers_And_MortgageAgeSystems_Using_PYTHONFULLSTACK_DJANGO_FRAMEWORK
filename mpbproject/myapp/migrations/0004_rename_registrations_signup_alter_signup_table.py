# Generated by Django 4.1.7 on 2023-03-29 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_registration_registrations_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registrations',
            new_name='Signup',
        ),
        migrations.AlterModelTable(
            name='signup',
            table='signup_table',
        ),
    ]