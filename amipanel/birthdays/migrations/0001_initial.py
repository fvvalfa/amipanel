# Generated by Django 4.0.6 on 2022-07-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('name', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'День рождения',
                'verbose_name_plural': 'Дни рождения',
                'db_table': 'birthdays',
                'ordering': ['day'],
            },
        ),
    ]
