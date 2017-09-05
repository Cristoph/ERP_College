from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from ModuleCommon.urls import api


urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

# API urls
urlpatterns += [
    # url(r'^api/', include(api.urls))
]


# ModuleCommon
urlpatterns += [
    url(r'^$', include('ModuleCommon.urls', namespace='ModuleCommon')),
]
# Login

from django.shortcuts import render
from django.views import View

class LoginView(View):
    template = 'login.html'

    def get(self, request):

        return render(request, self.template, locals())

urlpatterns += [
    url(r'^login', LoginView.as_view(), name='login'),
]

class AttorneyView(View):
    template = 'attorney/attorney.html'

    def get(self, request):

        return render(request, self.template, locals())

urlpatterns += [
    url(r'^attorney', AttorneyView.as_view(), name='attorney'),
]

class ReportView(View):
    template = 'report/report.html'

    def get(self, request):

        return render(request, self.template, locals())

urlpatterns += [
    url(r'^report', ReportView.as_view(), name='report'),
]
