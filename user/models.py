from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import BasePermission

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('reader', 'Reader'),
        ('writer', 'Writer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')

class IsReader(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'reader'

class IsWriter(IsReader):
    def has_permission(self, request, view):
        return request.user.role in ['writer', 'admin']

class IsAdmin(IsWriter):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
