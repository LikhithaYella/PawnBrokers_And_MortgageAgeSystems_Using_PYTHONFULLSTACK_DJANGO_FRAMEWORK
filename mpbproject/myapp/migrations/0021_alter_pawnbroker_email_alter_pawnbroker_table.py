# Generated by Django 4.1.7 on 2023-05-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_pawnbroker_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pawnbroker',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterModelTable(
            name='pawnbroker',
            table='pawnbrokers_table',
        ),
    ]
