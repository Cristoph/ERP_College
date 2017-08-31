from django.conf.urls import url
from .views import StudentQualifications

# Normal Url
urlpatterns = [
    url(r'^qualifications', StudentQualifications.as_view(), name='student-qualifications'),

]