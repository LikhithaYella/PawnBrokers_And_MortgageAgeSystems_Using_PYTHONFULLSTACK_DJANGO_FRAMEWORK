# Generated by Django 4.1.7 on 2023-05-06 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_pawnbroker_gender_alter_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
