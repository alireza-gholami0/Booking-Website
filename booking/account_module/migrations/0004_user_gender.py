# Generated by Django 4.2.3 on 2023-07-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_user_address_user_birth_date_user_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]