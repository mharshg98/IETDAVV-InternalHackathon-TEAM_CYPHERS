# Generated by Django 2.2.6 on 2020-01-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0015_auto_20200118_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
    ]
