# Generated by Django 4.2.2 on 2023-07-03 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_ad_ubication_alter_ad_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='population',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 1, 9, 9, 772151, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
    ]
