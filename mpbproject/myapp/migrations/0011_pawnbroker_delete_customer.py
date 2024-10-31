# Generated by Django 4.1.7 on 2023-04-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PawnBroker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Home', 'Home'), ('Jewelry', 'Jewelry'), ('Electronics', 'Electronics'), ('Clothes', 'Clothers'), ('Others', 'Others')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='productimages')),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
