# Generated by Django 4.1.7 on 2023-03-29 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_registration_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration',
            new_name='Registrations',
        ),
        migrations.AlterModelTable(
            name='registrations',
            table='registrations_table',
        ),
    ]
