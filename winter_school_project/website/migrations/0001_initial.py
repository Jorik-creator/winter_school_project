# Generated by Django 5.1.5 on 2025-01-24 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('points_price', models.IntegerField()),
                ('days_duration', models.PositiveSmallIntegerField()),
                ('last_day_offered', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.TextField()),
                ('document_type', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('location_lat', models.FloatField(null=True)),
                ('location_long', models.FloatField(null=True)),
                ('address_text', models.TextField(null=True)),
                ('social_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.TextField()),
                ('document_type', models.PositiveSmallIntegerField()),
                ('unofficial_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo_file', models.BinaryField(null=True)),
                ('logo_content_type', models.CharField(max_length=127, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Predefined_Skill',
            fields=[
                ('code', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Predefined_Task_Trait',
            fields=[
                ('code', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task_Category',
            fields=[
                ('code', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('min_points', models.IntegerField()),
                ('max_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Health_Vulnerability_Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_document_file', models.BinaryField()),
                ('content_type', models.CharField(max_length=127)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
        migrations.CreateModel(
            name='Benefits_Acquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_valid_since', models.DateField()),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.benefit')),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Custom_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField()),
                ('social_media_type', models.PositiveSmallIntegerField()),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
        migrations.AddField(
            model_name='benefit',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.organization'),
        ),
        migrations.CreateModel(
            name='Organization_Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_text', models.TextField()),
                ('location_lat', models.FloatField(null=True)),
                ('location_long', models.FloatField(null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField()),
                ('social_media_type', models.PositiveSmallIntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Predefined_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
                ('skill_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.predefined_skill')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location_lat', models.FloatField(null=True)),
                ('location_long', models.FloatField(null=True)),
                ('address_text', models.TextField(null=True)),
                ('datetime_created', models.DateTimeField()),
                ('datetime_planned', models.DateTimeField()),
                ('status', models.PositiveSmallIntegerField()),
                ('asking_individual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.individual')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.task_category')),
            ],
        ),
        migrations.CreateModel(
            name='Predefined_Trait_Of_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.predefined_task_trait')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.task')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Custom_Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.task')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Needed_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual_predefined_skill')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.task')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.task')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability_Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulnerability_type', models.PositiveSmallIntegerField()),
                ('proof_document_number', models.TextField()),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.individual')),
            ],
        ),
    ]
