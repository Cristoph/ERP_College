from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """model to represent additional information about users"""
    user = models.OneToOneField(User, related_name='profile')
    # The rest is completely
    gender = models.CharField(max_length=1, choices=(('H','Hombre'),('M','Mujer')), blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user



# class Person(models.Model):
#     rut = models.CharField(max_length=10, unique=True)
#     first_name = models.CharField(max_length=30, null=False)
#     last_name = models.CharField(max_length=30, null=False)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         abstract = True
#
#
# class Attorney(Person):
#     # custom fields
#     def __str__(self):
#         return self.rut
#
#
# class Student(Person):
#     attorney = models.ForeignKey(Attorney, null=False, blank=True, on_delete=models.CASCADE)
#     # level=models.CharField()
#
#     def __str__(self):
#         return self.rut
#
#
# class Teacher(Person):
#     # custom fields
#
#     def __str__(self):
#         return self.rut
#
#
# class Administrative(Person):
#     # custom fields
#
#     def __str__(self):
#         return self.rut
