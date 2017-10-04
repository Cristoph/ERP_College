from django.db import models

# crear modelos relacionados a las funciones del docente, subir notas, anotaciones, ver ramos asignados, etc
# *modelo de ramos y cursos en ModuelCommon

class Trans(models.Model):
    obj1 = models.TextField(null=False, blank=True)
    obj2 = models.CharField(max_length=250, null=False, blank=True)
    obj3 = models.CharField(max_length=250, null=False, blank=True)
    obj4 = models.CharField(max_length=250, null=False, blank=True)
    obj5 = models.CharField(max_length=250, null=False, blank=True)
    obj6 = models.CharField(max_length=250, null=False, blank=True)
    obj7 = models.CharField(max_length=250, null=False, blank=True)
    obj8 = models.CharField(max_length=250, null=False, blank=True)
    obj9 = models.CharField(max_length=250, null=False, blank=True)
    obj10 = models.CharField(max_length=250, null=False, blank=True)
    obj11 = models.CharField(max_length=250, null=False, blank=True)
    obj12 = models.CharField(max_length=250, null=False, blank=True)
    obj13 = models.CharField(max_length=250, null=False, blank=True)
    obj14 = models.CharField(max_length=250, null=False, blank=True)
    obj15 = models.CharField(max_length=250, null=False, blank=True)
    obj16 = models.CharField(max_length=250, null=False, blank=True)
    obj17 = models.CharField(max_length=250, null=False, blank=True)
    obj18 = models.CharField(max_length=250, null=False, blank=True)
    obj19 = models.CharField(max_length=250, null=False, blank=True)
    obj20 = models.CharField(max_length=250, null=False, blank=True)