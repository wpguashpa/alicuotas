# Generated by Django 4.2.2 on 2023-06-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_ad_auction_date_alter_ad_cadastral_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='auction_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='cadastral_key',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='characteristics',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='construction_area',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='limit',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='property_area',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='property_type',
            field=models.TextField(null=True, verbose_name=100),
        ),
        migrations.AlterField(
            model_name='ad',
            name='signaling',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
