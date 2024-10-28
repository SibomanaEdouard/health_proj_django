from django.db import models
from django.utils import timezone
import uuid

# this is entity for the medical 
class MedicalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # patient = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    # doctor = models.ForeignKey('users.Doctor', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    diagnosis = models.TextField()
    prescription = models.TextField()
    attachments = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'medical_record'

class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name='prescriptions'  # Add this line
    )
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
        db_table = 'prescriptions'

# this is the entity for test 
class LabTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    test_date = models.DateField()
    results = models.TextField()
    attachment = models.FileField(upload_to='lab_results/', null=True, blank=True)

    class Meta:
        db_table = 'lab_test'