from django.contrib import admin
from .models import MedicalRecord , Prescription , LabTest

# Register your models here.
admin.site.register(MedicalRecord)
admin.site.register(Prescription)
admin.site.register(LabTest)

