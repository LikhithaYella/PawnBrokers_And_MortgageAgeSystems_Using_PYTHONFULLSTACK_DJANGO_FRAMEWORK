# Generated by Django 4.1.7 on 2023-03-31 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_registrations_signup_alter_signup_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='Registration',
        ),
        migrations.AlterModelTable(
            name='registration',
            table='registration_table',
        ),
    ]
