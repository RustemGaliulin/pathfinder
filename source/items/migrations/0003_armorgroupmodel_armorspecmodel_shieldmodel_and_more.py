# Generated by Django 5.1.1 on 2024-11-11 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_descriptormodel_itemmodel_descriptors'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmorGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArmorSpecModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShieldModel',
            fields=[
                ('itemmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.itemmodel')),
                ('armor_bonus', models.IntegerField()),
                ('extra_armor_bonus', models.IntegerField()),
                ('speed_penalty', models.IntegerField()),
                ('hardness', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('break_limit', models.IntegerField()),
            ],
            bases=('items.itemmodel',),
        ),
        migrations.CreateModel(
            name='WeaponGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('critical_hit_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='descriptors',
            field=models.ManyToManyField(related_name='items', to='items.descriptormodel'),
        ),
        migrations.CreateModel(
            name='ArmorModel',
            fields=[
                ('itemmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.itemmodel')),
                ('category', models.CharField()),
                ('armor_class_bonus', models.IntegerField()),
                ('dex_cap', models.IntegerField()),
                ('check_penalty', models.IntegerField()),
                ('speed_penalty', models.IntegerField()),
                ('str', models.IntegerField()),
                ('group', models.ManyToManyField(related_name='armors', to='items.armorgroupmodel')),
                ('spec_effect', models.ManyToManyField(related_name='armors', to='items.armorspecmodel')),
            ],
            bases=('items.itemmodel',),
        ),
        migrations.CreateModel(
            name='WeaponModel',
            fields=[
                ('itemmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.itemmodel')),
                ('damage', models.CharField()),
                ('damage_type', models.CharField()),
                ('hands', models.FloatField()),
                ('tag', models.ManyToManyField(related_name='weapons', to='items.weapongroupmodel')),
            ],
            bases=('items.itemmodel',),
        ),
    ]
