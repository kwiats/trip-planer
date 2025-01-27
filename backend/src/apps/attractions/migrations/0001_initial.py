# Generated by Django 4.2 on 2025-01-27 00:32

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'categories',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('open_hours', models.JSONField(blank=True, help_text='\n        {\n            "monday": ["08:00", "17:00"],\n            "tuesday": ["08:00", "17:00"],\n            "wednesday": ["08:00", "17:00"],\n            "thursday": ["08:00", "17:00"],\n            "friday": ["08:00", "17:00"],\n            "saturday": ["08:00", "17:00"],\n            "sunday": ["08:00", "17:00"]}\n    ', null=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('categories', models.ManyToManyField(blank=True, related_name='attractions', to='attractions.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'attraction',
                'verbose_name_plural': 'attractions',
                'db_table': 'attractions',
            },
        ),
        migrations.AddConstraint(
            model_name='attraction',
            constraint=models.UniqueConstraint(fields=('name', 'longitude', 'latitude'), name='unique_attraction'),
        ),
    ]
