from django.conf.urls import url
from .views import StudentQualifications, StudentReport

# Normal Url
urlpatterns = [
    url(r'^qualifications', StudentQualifications.as_view(), name='student-qualifications'),
    url(r'^report', StudentReport.as_view(), name='student-report'),

]