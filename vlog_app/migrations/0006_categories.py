# Generated by Django 5.1.2 on 2024-11-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0005_vlogpost_published_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42, unique=True)),
            ],
        ),
    ]
