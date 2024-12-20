# Generated by Django 5.1.1 on 2024-11-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='descriptors',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='items.descriptormodel'),
        ),
    ]
