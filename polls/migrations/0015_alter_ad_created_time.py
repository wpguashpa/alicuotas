# Generated by Django 4.2.2 on 2023-07-03 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_ad_category_alter_ad_created_time_alter_media_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 16, 35, 5, 507958, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
    ]
