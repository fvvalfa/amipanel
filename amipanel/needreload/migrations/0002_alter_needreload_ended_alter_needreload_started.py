# Generated by Django 4.0.6 on 2022-08-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needreload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needreload',
            name='ended',
            field=models.DateTimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='needreload',
            name='started',
            field=models.DateTimeField(auto_now=True, verbose_name='Начало'),
        ),
    ]
