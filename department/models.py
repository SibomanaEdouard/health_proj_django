from django.db import models
import uuid


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # head_doctor = models.ForeignKey(
    #     'users.Doctor',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='headed_departments' 
    # )

    class Meta:
        db_table = 'department'

class Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    departments = models.ManyToManyField(Department)

    class Meta:
        db_table = 'hospital'