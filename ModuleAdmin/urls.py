from django.conf.urls import url
from .views import AdminGrades, AdminSubjects, AdminTeachers, AdminStudents

urlpatterns = [
    url(r'^grades', AdminGrades.as_view(), name='grades'),
    url(r'^subjects', AdminSubjects.as_view(), name='subjects'),
    url(r'^eachers', AdminTeachers.as_view(), name='teachers'),
    url(r'^students', AdminStudents.as_view(), name='students'),
]

