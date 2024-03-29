# Generated by Django 5.0.2 on 2024-02-09 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society_Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('google_map', models.CharField(blank=True, max_length=1000, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.city')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.locality')),
            ],
            options={
                'verbose_name_plural': '1. Society_Building',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.society_building')),
            ],
            options={
                'verbose_name_plural': '2. Images',
            },
        ),
    ]
