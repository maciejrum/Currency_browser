# Generated by Django 4.2.1 on 2023-05-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_remove_currencyname_currency_names_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencydate',
            name='currency_names',
        ),
        migrations.RemoveField(
            model_name='currencydate',
            name='exchange_rate',
        ),
        migrations.AddField(
            model_name='currencyvalue',
            name='currency_dates',
            field=models.ManyToManyField(related_name='currency_values', to='currency.currencydate'),
        ),
    ]
