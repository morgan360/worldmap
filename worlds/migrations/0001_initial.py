# Generated by Django 4.2.3 on 2024-02-13 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('supertype', models.CharField(blank=True, max_length=255, null=True)),
                ('subtype', models.CharField(blank=True, max_length=255, null=True)),
                ('creation_time_stamp', models.IntegerField()),
                ('image_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('supertype', models.CharField(blank=True, max_length=255, null=True)),
                ('subtype', models.CharField(blank=True, max_length=255, null=True)),
                ('creation_time_stamp', models.IntegerField()),
                ('image_url', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('physicality', models.TextField(blank=True, null=True)),
                ('traits', models.TextField(blank=True, null=True)),
                ('languages', models.TextField(blank=True, null=True)),
                ('abilities', models.TextField(blank=True, null=True)),
                ('appearance', models.TextField(blank=True, null=True)),
                ('background', models.TextField(blank=True, null=True)),
                ('motivations', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('charisma', models.IntegerField(blank=True, null=True)),
                ('coercion', models.IntegerField(blank=True, null=True)),
                ('capability', models.IntegerField(blank=True, null=True)),
                ('compassion', models.IntegerField(blank=True, null=True)),
                ('creativity', models.IntegerField(blank=True, null=True)),
                ('courage', models.IntegerField(blank=True, null=True)),
                ('corruption', models.TextField(blank=True, null=True)),
                ('titles', models.TextField(blank=True, null=True)),
                ('institutions', models.TextField(blank=True, null=True)),
                ('events', models.TextField(blank=True, null=True)),
                ('family', models.TextField(blank=True, null=True)),
                ('friends', models.TextField(blank=True, null=True)),
                ('rivals', models.TextField(blank=True, null=True)),
                ('relations', models.TextField(blank=True, null=True)),
                ('hit_points', models.IntegerField(blank=True, null=True)),
                ('alignment', models.TextField(blank=True, null=True)),
                ('inspirations', models.TextField(blank=True, null=True)),
                ('tt_str', models.IntegerField(blank=True, null=True)),
                ('tt_int', models.IntegerField(blank=True, null=True)),
                ('tt_con', models.IntegerField(blank=True, null=True)),
                ('tt_dex', models.IntegerField(blank=True, null=True)),
                ('tt_wis', models.IntegerField(blank=True, null=True)),
                ('tt_cha', models.IntegerField(blank=True, null=True)),
                ('skill_stealth', models.IntegerField(blank=True, null=True)),
                ('equipment', models.TextField(blank=True, null=True)),
                ('backpack', models.TextField(blank=True, null=True)),
                ('proficiencies', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('spells', models.TextField(blank=True, null=True)),
                ('birthplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='worlds.location')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='worlds.location')),
            ],
        ),
    ]