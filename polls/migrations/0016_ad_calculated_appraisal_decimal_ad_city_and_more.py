# Generated by Django 4.2.2 on 2023-07-06 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_ad_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='calculated_appraisal_decimal',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='city',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='expert_appraisal_decimal',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 2, 6, 13, 556359, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
    ]
