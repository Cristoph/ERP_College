from django.conf.urls import url
from .views import HomeView
# from tastypie.api import Api
# from .api import AttorneyResource, StudentResource, TeacherResource, AdministrativeResource
# from .views import AttorneyListView, AttorneyDetailView
# from .views import StudentListView, StudentDetailView
# from .views import TeacherListView, StudentDetailView
# from .views import AdministrativeListView, AdministrativeDetailView


# API conf
# api = Api(api_name='v1')
# api.register(AttorneyResource())
# api.register(StudentResource())
# api.register(TeacherResource())
# api.register(AdministrativeResource())


# Normal Url
urlpatterns = [
    url(r'$', HomeView.as_view(), name='common-home'),

    # url(r'attorney/$', AttorneyListView.as_view(), name='attorney-list'),
    # url(r'^attorney/(?P<slug>[-_\w]+)/$', AttorneyDetailView.as_view(), name='attorney-detail'),
]