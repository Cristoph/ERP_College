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

# ModuleTeacher
urlpatterns += [
    url(r'^teacher/', include('ModuleTeacher.urls', namespace='module_teacher')),
]

# ModuleAdmin
urlpatterns += [
    url(r'^administrator/', include('ModuleAdmin.urls', namespace='module_admin')),
]
