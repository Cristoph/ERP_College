from django.conf.urls import url
from tastypie.api import Api
from .api import AttorneyResource, StudentResource, TeacherResource, AdministrativeResource

# API conf
api = Api(api_name='v1')
api.register(AttorneyResource())
api.register(StudentResource())
api.register(TeacherResource())
api.register(AdministrativeResource())


# Normal Url
