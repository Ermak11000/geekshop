# Generated by Django 3.2.12 on 2022-04-27 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 14, 43, 15, 905234, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
