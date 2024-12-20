# Generated by Django 5.1.1 on 2024-10-24 06:20

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=200)),
                ('test_date', models.DateField()),
                ('results', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='lab_results/')),
            ],
            options={
                'db_table': 'lab_test',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
                ('attachments', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medical_record',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('medication_name', models.CharField(max_length=200)),
                ('dosage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'prescriptions',
            },
        ),
    ]
