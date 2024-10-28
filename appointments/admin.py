from django.contrib import admin
from .models import  Appointment , AppointmentReminder

admin.site.register(Appointment)
admin.site.register(AppointmentReminder)
