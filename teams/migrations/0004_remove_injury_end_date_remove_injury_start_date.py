# Generated by Django 4.2.9 on 2024-01-31 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_injury_end_date_alter_injury_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injury',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='start_date',
        ),
    ]
