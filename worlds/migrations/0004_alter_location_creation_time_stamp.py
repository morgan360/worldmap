# Generated by Django 4.2.3 on 2024-02-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0003_alter_location_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='creation_time_stamp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
