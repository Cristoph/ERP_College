from django.conf.urls import url
from .views import TeacherSchedules, TeacherQualifications, TeacherAssistances, TeacherAnnotations, TeacherQualificationsSet

urlpatterns = [
    url(r'^schedules', TeacherSchedules.as_view(), name='schedules'),
    url(r'^qualifications/$', TeacherQualifications.as_view(), name='qualifications'),
    url(r'^qualifications/(?P<grade>\d+)/(?P<subject>\d+)/(?P<edit>\w+)$', TeacherQualificationsSet.as_view(), name='qualifications_set'),
    url(r'^assistances', TeacherAssistances.as_view(), name='assistances'),
    url(r'^annotations', TeacherAnnotations.as_view(), name='annotations'),

]
