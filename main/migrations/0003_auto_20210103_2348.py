# Generated by Django 3.1.4 on 2021-01-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210103_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Toppings'},
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
