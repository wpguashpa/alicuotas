# Generated by Django 4.2.2 on 2023-07-18 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_ad_calculated_appraisal_decimal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='subtitle',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='calculated_appraisal_decimal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='AvCalcu'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 22, 44, 9, 658733, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='expert_appraisal_decimal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='AvPericial'),
        ),
    ]
