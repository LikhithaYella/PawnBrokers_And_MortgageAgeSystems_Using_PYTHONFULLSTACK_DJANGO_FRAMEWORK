# Generated by Django 4.1.7 on 2023-04-03 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_addpawnbroker_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddPawnBroker',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]