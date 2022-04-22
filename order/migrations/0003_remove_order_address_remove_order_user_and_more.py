# Generated by Django 4.0.2 on 2022-04-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
        ('order', '0002_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
            preserve_default=False,
        ),
    ]