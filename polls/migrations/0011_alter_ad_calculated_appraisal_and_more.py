# Generated by Django 4.2.2 on 2023-06-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_ad_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='calculated_appraisal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='expert_appraisal',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
