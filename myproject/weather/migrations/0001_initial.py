# Generated by Django 5.0.3 on 2024-03-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
