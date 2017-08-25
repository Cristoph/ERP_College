from django.conf.urls import url, include
from django.contrib import admin
from ModuleCommon.urls import api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# API urls
urlpatterns += [
    url(r'^api/', include(api.urls))
]


# ModuleCommon
# urlpatterns += [
#     url(r'^module-common/', include('ModuleCommon.urls', namespace='ModuleCommon')),
# ]
#


