# Generated by Django 2.1.1 on 2018-09-29 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180929_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 23, 26, 17, 125449)),
        ),
    ]
