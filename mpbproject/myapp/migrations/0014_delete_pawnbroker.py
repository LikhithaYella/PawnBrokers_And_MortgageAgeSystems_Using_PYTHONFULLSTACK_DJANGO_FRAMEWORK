# Generated by Django 4.1.7 on 2023-04-03 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_pawnbroker_price_alter_pawnbroker_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PawnBroker',
        ),
    ]
