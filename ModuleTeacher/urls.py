from django.conf.urls import url
from .views import TeacherSchedules, TeacherQualifications, TeacherAssistances, TeacherAnnotations

urlpatterns = [
    url(r'^schedules', TeacherSchedules.as_view(), name='schedules'),
    url(r'^qualifications', TeacherQualifications.as_view(), name='qualifications'),
    url(r'^assistances', TeacherAssistances.as_view(), name='assistances'),
    url(r'^annotations', TeacherAnnotations.as_view(), name='annotations'),

]
