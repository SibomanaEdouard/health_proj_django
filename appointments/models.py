from django.db import models
# from users.models import Patient, Doctor
import uuid

# model for the appointmenst 
class Appointment(models.Model):
    # this is scheduling of the appointment
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # patient = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    # doctor = models.ForeignKey('users.Doctor', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'appointment'



# this is the reminder 
class AppointmentReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    sent = models.BooleanField(default=False)
    class Meta:
        db_table = 'appointment_reminder'   