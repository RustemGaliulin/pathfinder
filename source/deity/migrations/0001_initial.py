# Generated by Django 5.1.1 on 2024-11-25 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('char', '0003_backgroundmodel_heritagemodel_proficiency'),
        ('skills', '0002_perceptionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevoteeSpellsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_criteria', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DivineIntercessionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minor_boon', models.TextField()),
                ('moderate_boon', models.TextField()),
                ('major_boon', models.TextField()),
                ('minor_curse', models.TextField()),
                ('moderate_curse', models.TextField()),
                ('major_curse', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DomainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DevoteeBenefitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.CharField(blank=True)),
                ('ability', models.ManyToManyField(related_name='devotee_benefits', to='char.abilitiesmodel')),
                ('skill', models.ManyToManyField(related_name='devotee_benefits', to='skills.skillmodel')),
                ('devotee_spells', models.ManyToManyField(related_name='devotee_benefits', to='deity.devoteespellsmodel')),
                ('alternate_domain', models.ManyToManyField(related_name='devotee_benefits_alternate', to='deity.domainmodel')),
                ('domain', models.ManyToManyField(related_name='devotee_benefits', to='deity.domainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DeityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('title', models.CharField()),
                ('description', models.TextField()),
                ('category', models.CharField()),
                ('edicts', models.TextField()),
                ('anathema', models.TextField()),
                ('areas_of_concern', models.TextField()),
                ('pantheons', models.TextField()),
                ('followers_alignment', models.CharField(blank=True, choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('TN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], max_length=2, null=True)),
                ('devotees', models.TextField(blank=True)),
                ('animal', models.CharField(blank=True)),
                ('allies', models.ManyToManyField(to='deity.deitymodel')),
                ('enemies', models.ManyToManyField(to='deity.deitymodel')),
                ('devotee_benefits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deity.devoteebenefitmodel')),
                ('divine_intercession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deity.divineintercessionmodel')),
            ],
        ),
    ]