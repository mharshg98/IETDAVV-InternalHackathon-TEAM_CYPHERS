# Generated by Django 2.2.6 on 2020-01-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0023_auto_20200122_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribaluser',
            name='mobile',
            field=models.CharField(default=' ', max_length=10),
        ),
    ]
