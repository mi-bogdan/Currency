# Generated by Django 4.0.4 on 2022-07-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valute',
            name='from_curr',
            field=models.CharField(max_length=10, verbose_name='из_какой_вылюты'),
        ),
        migrations.AlterField(
            model_name='valute',
            name='to_curr',
            field=models.CharField(max_length=10, verbose_name='в_какую_валюту'),
        ),
        migrations.DeleteModel(
            name='CurrValute',
        ),
    ]
