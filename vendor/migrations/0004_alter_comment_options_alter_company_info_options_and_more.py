# Generated by Django 5.0.2 on 2024-02-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_company_info_options_remove_comment_ip_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '13. Comment'},
        ),
        migrations.AlterModelOptions(
            name='company_info',
            options={'verbose_name_plural': '2. Company Info'},
        ),
        migrations.AlterModelOptions(
            name='dealin',
            options={'verbose_name_plural': '5. keywords'},
        ),
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name_plural': '3. Error'},
        ),
        migrations.AlterModelOptions(
            name='follow_up',
            options={'verbose_name_plural': '10. Follow_Up'},
        ),
        migrations.AlterModelOptions(
            name='meeting',
            options={'verbose_name_plural': '11. Meeting'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': '6. Social'},
        ),
        migrations.AlterModelOptions(
            name='user_comment',
            options={'verbose_name_plural': '4. User_Comment'},
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name_plural': '12. Visit'},
        ),
    ]
