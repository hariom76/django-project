# Generated by Django 3.0.2 on 2020-01-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0003_orderdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
