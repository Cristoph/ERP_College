from django.conf.urls import url
from .views import AdminGrades, AdminSubjects, AdminTeachers, AdminStudents, AdminAdmissionAttorney,\
    AdminAdmissionStudentSet, AdminAdmissionAttorneySet, AdminAdmissionStudent, AdminAdmissionenRollmentSet

urlpatterns = [
    url(r'^grades', AdminGrades.as_view(), name='grades'),
    url(r'^subjects', AdminSubjects.as_view(), name='subjects'),
    url(r'^eachers', AdminTeachers.as_view(), name='teachers'),
    url(r'^students', AdminStudents.as_view(), name='students'),
    url(r'^admission/$', AdminAdmissionAttorney.as_view(), name='admission_attorney'),
    url(r'^admission/(?P<rut>[a-z0-9,-]+)$', AdminAdmissionAttorneySet.as_view(), name='admission_attorney_set'),
    url(r'^student/(?P<rut>[a-z0-9,-]+)/$', AdminAdmissionStudent.as_view(), name='admission_student'),
    url(r'^student/(?P<rut>[a-z0-9,-]+)/(?P<student>[a-z0-9,-]+)/$', AdminAdmissionStudentSet.as_view(), name='admission_student_set'),
    url(r'^enrollment/(?P<rut>[a-z0-9,-]+)/(?P<student>[a-z0-9,-]+)/$', AdminAdmissionenRollmentSet.as_view(), name='admission_enrollment_set'),
]

