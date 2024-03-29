# Generated by Django 5.0.2 on 2024-02-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_company_address_company_call_status_company_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='call_comment',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='call_status',
            field=models.CharField(choices=[('New', 'New'), ('Foloow_Up', 'Foloow_Up'), ('Meeting', 'Meeting'), ('Deal_Done', 'Deal_Done'), ('Call Not Receive', 'Call Not Receive'), ('Not Interested', 'Not Interested'), ('Deal_Done', 'Deal_Done'), ('Call Cut', 'Call Cut')], default='New', max_length=50),
        ),
    ]
