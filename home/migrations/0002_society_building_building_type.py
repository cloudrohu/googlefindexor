# Generated by Django 5.0.2 on 2024-02-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='society_building',
            name='building_type',
            field=models.CharField(choices=[('Residential', 'Residential'), ('commercial ', 'commercial ')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]