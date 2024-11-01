# Generated by Django 4.1.7 on 2023-05-06 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20230506_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='pawnbroker',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], default=datetime.datetime(2023, 5, 6, 16, 31, 36, 954457), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Prefer not to say')], default='M', max_length=10),
        ),
    ]
