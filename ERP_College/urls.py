from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

# Basic Login
urlpatterns += [
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]


# API urls
# urlpatterns += [
#     url(r'^api/', include(api.urls))
# ]


# ModuleCommon
urlpatterns += [
    url(r'^', include('ModuleCommon.urls', namespace='module_common')),
]


# ModuleStudent
urlpatterns += [
    url(r'^student/', include('ModuleStudent.urls', namespace='module_student')),
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
