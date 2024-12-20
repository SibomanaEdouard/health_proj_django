# Generated by Django 5.1.1 on 2024-10-24 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_records', '0001_initial'),
        ('users', '0002_doctor_nurse_patient_user_delete_users_patient_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
        migrations.AddField(
            model_name='labtest',
            name='medical_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_records.medicalrecord'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medical_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='medical_records.medicalrecord'),
        ),
    ]
