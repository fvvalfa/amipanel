# Generated by Django 4.0.6 on 2022-08-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_events_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='important',
            field=models.BooleanField(default=False, null=True, verbose_name='Важное событие'),
        ),
    ]
