# Generated by Django 5.1.1 on 2024-11-25 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char', '0003_backgroundmodel_heritagemodel_proficiency'),
        ('deity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactermodel',
            name='deity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deity.deitymodel'),
        ),
        migrations.AddField(
            model_name='charactermodel',
            name='saving_throw_notes',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='charactermodel',
            name='background',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='char.backgroundmodel'),
        ),
        migrations.AddField(
            model_name='heritagemodel',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heritages', to='char.racemodel'),
        ),
        migrations.AddField(
            model_name='charactermodel',
            name='heritage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='chars', to='char.heritagemodel'),
        ),
    ]
