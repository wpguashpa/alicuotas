# Generated by Django 4.2.2 on 2023-07-01 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_ad_calculated_appraisal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='ubication',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]
