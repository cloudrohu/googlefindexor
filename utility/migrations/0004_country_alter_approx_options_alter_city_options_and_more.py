# Generated by Django 5.0.2 on 2024-02-10 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0003_alter_keywords_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '9. Country',
            },
        ),
        migrations.AlterModelOptions(
            name='approx',
            options={'verbose_name_plural': '3. Approx'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': '7. City'},
        ),
        migrations.AlterModelOptions(
            name='keywords',
            options={'verbose_name_plural': '1. Key_Words'},
        ),
        migrations.AlterModelOptions(
            name='locality',
            options={'verbose_name_plural': '10. Locality'},
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.country')),
            ],
            options={
                'verbose_name_plural': '8. State',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.state'),
        ),
    ]
