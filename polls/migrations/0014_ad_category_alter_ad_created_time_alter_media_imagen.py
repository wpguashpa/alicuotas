# Generated by Django 4.2.2 on 2023-07-03 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_ad_population_alter_ad_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 16, 34, 55, 774666, tzinfo=datetime.timezone.utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='media',
            name='imagen',
            field=models.FileField(upload_to='images/remates/'),
        ),
    ]
