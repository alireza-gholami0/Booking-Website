# Generated by Django 4.2.3 on 2023-07-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
