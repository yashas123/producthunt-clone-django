# Generated by Django 2.1.8 on 2019-05-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190522_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='userinputs',
            options={'verbose_name_plural': 'User Inputs'},
        ),
    ]
