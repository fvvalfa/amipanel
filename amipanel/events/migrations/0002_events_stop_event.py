# Generated by Django 4.0.6 on 2022-07-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='stop_event',
            field=models.DateTimeField(null=True, verbose_name='Окончание события'),
        ),
    ]
