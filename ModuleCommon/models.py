from django.db import models


class Person(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Attorney(Person):
    # custom fields
    def __str__(self):
        return self.rut


class Student(Person):
    attorney = models.ForeignKey(Attorney, null=False, blank=True, on_delete=models.CASCADE)
    # level=models.CharField()

    def __str__(self):
        return self.rut


class Teacher(Person):
    # custom fields

    def __str__(self):
        return self.rut


class Administrative(Person):
    # custom fields

    def __str__(self):
        return self.rut
