# Generated by Django 4.1.2 on 2022-11-23 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_updateuser_confirm_transaction_pin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateuser',
            name='confirm_transaction_pin',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='updateuser',
            name='transaction_pin',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
