# Generated by Django 5.1.2 on 2024-11-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0003_alter_vlogpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlogpost',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]