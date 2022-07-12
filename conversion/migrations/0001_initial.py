# Generated by Django 4.0.4 on 2022-07-07 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrValute',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name_curr', models.CharField(
                    max_length=20, verbose_name='Из-какой валюты')),
            ],
            options={
                'verbose_name': 'Валюта_стран',
                'verbose_name_plural': 'Валюты_стран',
            },
        ),
        migrations.CreateModel(
            name='Valute',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('from_amount', models.IntegerField(verbose_name='Число')),
                ('converted_amount', models.FloatField(verbose_name='Сумма')),
                ('data_converted', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата операции')),
                ('from_curr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                 related_name='from_curr', to='conversion.currvalute', verbose_name='из-какой валыты')),
                ('to_curr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                 related_name='to_curr', to='conversion.currvalute', verbose_name='в какую валюту')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
    ]