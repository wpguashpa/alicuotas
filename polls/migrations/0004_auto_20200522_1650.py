# Generated by Django 3.1a1 on 2020-05-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200522_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message_id',
            field=models.CharField(max_length=100),
        ),
    ]
