from django.conf.urls import url
from .views import ReportQualifications

# Normal Url
urlpatterns = [
    url(r'^qualifications/(?P<pk>\d+)$', ReportQualifications.as_view(), name='report-qualifications'),

]