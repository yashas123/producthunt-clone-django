# Generated by Django 2.1.1 on 2018-09-29 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180929_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_udate',
            new_name='modified_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 23, 31, 12, 871909)),
        ),
    ]