from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    rut = models.CharField(max_length=12, null=False)
    date_of_birth = models.DateTimeField()
    level=models.CharField()
    attorney = models.ForeignKey(Attorney, null=False, blank=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Attorney(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    rut = models.CharField(max_length=12, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)