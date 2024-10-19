from django.db import models
from django.utils import timezone

# This is user models
class Users(models.Model):
    uuid = models.UUIDField()
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.TextField(max_length=255, null=False)
    email = models.EmailField(max_length=255,null=False,unique=True)
    phone = models.TextField(max_length=10,null=False,unique=True)
    password = models.CharField(null=False)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)
    role = models.TextField(default='USER')
    
class Meta:
    db_table='users'

