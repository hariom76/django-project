# Generated by Django 3.0.2 on 2020-01-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0002_registration_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.CharField(max_length=3, null=True)),
                ('order_name', models.CharField(max_length=3, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]