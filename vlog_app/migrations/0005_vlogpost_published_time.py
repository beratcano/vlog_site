# Generated by Django 5.1.2 on 2024-11-20 20:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0004_alter_vlogpost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlogpost',
            name='published_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
