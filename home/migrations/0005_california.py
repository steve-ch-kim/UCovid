# Generated by Django 3.0.7 on 2020-09-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200928_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='California',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cases', models.PositiveIntegerField()),
                ('new_cases', models.PositiveIntegerField(default=0)),
                ('total_deaths', models.PositiveIntegerField()),
                ('new_deaths', models.PositiveIntegerField(default=0)),
                ('total_tests', models.PositiveIntegerField()),
            ],
        ),
    ]
