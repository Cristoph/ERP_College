from django.conf.urls import url
from .views import ReportQualifications, EnrollmentReport

# Normal Url
urlpatterns = [
    url(r'^qualifications/(?P<id>\d+)$', ReportQualifications.as_view(), name='report-qualifications'),

    url(r'^enrollment/(?P<id>\d+)$', EnrollmentReport.as_view(), name='enrollment-report'),

]