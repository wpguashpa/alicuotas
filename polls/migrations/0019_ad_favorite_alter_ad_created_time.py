# Generated by Django 4.2.2 on 2023-08-09 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_ad_subtitle_alter_ad_calculated_appraisal_decimal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='favorite',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 20, 1, 13, 15061, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
    ]
