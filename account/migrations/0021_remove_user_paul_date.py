# Generated by Django 4.1.2 on 2023-01-20 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_user_paul_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='paul_date',
        ),
    ]