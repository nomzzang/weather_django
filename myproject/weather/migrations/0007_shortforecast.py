# Generated by Django 5.0.3 on 2024-03-26 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_delete_ultrashortforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseDate', models.CharField(max_length=8)),
                ('baseTime', models.CharField(max_length=4)),
                ('fcstDate', models.CharField(max_length=8)),
                ('fcstTime', models.CharField(max_length=4)),
                ('fcstValue', models.CharField(max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.location')),
            ],
        ),
    ]
