# Generated by Django 2.1.1 on 2018-09-30 08:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20180930_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='voter',
            field=models.ManyToManyField(related_name='voting_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='hunter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_hunter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 30, 14, 9, 53, 309481)),
        ),
    ]
