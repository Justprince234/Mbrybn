# Generated by Django 4.1.2 on 2022-11-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_updateuser_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
