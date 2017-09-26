from django.conf.urls import url
from .views import AdminGrades, AdminSubjects, AdminTeachers, AdminStudents, AdminAdmission,\
    AdminAdmissionStudent

urlpatterns = [
    url(r'^grades', AdminGrades.as_view(), name='grades'),
    url(r'^subjects', AdminSubjects.as_view(), name='subjects'),
    url(r'^eachers', AdminTeachers.as_view(), name='teachers'),
    url(r'^students', AdminStudents.as_view(), name='students'),
    url(r'^admission/$', AdminAdmission.as_view(), name='admission_attorney'),
    url(r'^admission/(?P<pk>[0-9,-]+)$', AdminAdmissionStudent.as_view(), name='admission_student'),
]

