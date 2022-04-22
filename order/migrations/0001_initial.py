# Generated by Django 4.0.2 on 2022-04-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('payment', models.BooleanField(default=False)),
                ('price_paid', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('trackingcode', models.BigIntegerField()),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]