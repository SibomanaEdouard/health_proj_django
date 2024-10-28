from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Administrator'),
        ('user','user')
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(choices=USER_TYPES,default='user')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permission_set',
        blank=True,
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return f"{self.get_full_name()} ({self.user_type})"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)


# class Patient(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='patient_profile'
#     )
#     date_of_birth = models.DateField()
#     blood_group = models.CharField(max_length=5)
#     emergency_contact = models.CharField(max_length=15)
#     address = models.TextField()
#     insurance_info = models.JSONField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'patient'

    # def __str__(self):
    #     return f"Patient: {self.user.get_full_name()}"

# class Doctor(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='doctor_profile'
#     )
#     specialization = models.CharField(max_length=100)
#     license_number = models.CharField(max_length=50, unique=True)
#     availability = models.JSONField(default=dict)
#     department = models.CharField(max_length=100)
#     consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'doctor'

#     def __str__(self):
#         return f"Dr. {self.user.get_full_name()}"


# class Nurse(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='nurse_profile'
#     )
#     department = models.CharField(max_length=100)
#     shift = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'nurse'

#     def __str__(self):
#         return f"Nurse: {self.user.get_full_name()}"