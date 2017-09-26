from django.conf.urls import url
from .views import HomeView
from tastypie.api import Api

# Normal Url
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='common-home'),

    # url(r'attorney/$', AttorneyListView.as_view(), name='attorney-list'),
    # url(r'^attorney/(?P<slug>[-_\w]+)/$', AttorneyDetailView.as_view(), name='attorney-detail'),
]
