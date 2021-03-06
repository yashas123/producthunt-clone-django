# Generated by Django 2.1.8 on 2019-05-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinputs',
            name='fav',
            field=models.ManyToManyField(related_name='user_favs', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='userinputs',
            name='liked',
            field=models.ManyToManyField(related_name='user_likes', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='userinputs',
            name='voted',
            field=models.ManyToManyField(related_name='user_votes', to='products.Product'),
        ),
    ]
