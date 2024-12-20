# Generated by Django 5.1.1 on 2024-11-05 18:18

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char', '0002_abilitiesmodel_healthmodel_sizemodel_and_more'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerceptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_bonus', models.IntegerField()),
                ('item_bonus', models.IntegerField()),
                ('senses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=15)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='char.charactermodel')),
                ('proficiency_bonus', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='skills.proficiencymodel')),
            ],
        ),
    ]
