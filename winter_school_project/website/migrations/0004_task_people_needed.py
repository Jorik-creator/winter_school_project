# Generated by Django 5.1.5 on 2025-01-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_task_points_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='people_needed',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
