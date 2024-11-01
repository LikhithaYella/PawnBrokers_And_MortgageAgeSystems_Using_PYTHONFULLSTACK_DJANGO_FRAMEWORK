# Generated by Django 4.1.7 on 2023-05-07 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_admin_created_at_admin_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pawnbroker',
            old_name='salary',
            new_name='income',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='pawnbroker',
            name='dateofbirth',
        ),
        migrations.AddField(
            model_name='pawnbroker',
            name='loanprovided',
            field=models.PositiveIntegerField(default=datetime.datetime(2023, 5, 7, 6, 12, 20, 189679)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pawnbroker',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='pawnbroker',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pawnbroker',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pawnbroker',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
