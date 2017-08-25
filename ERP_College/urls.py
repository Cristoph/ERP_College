from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ModuleCommon.urls import api


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
    url(r'^api/', include(api.urls))
]


# ModuleCommon
# urlpatterns += [
#     url(r'^module-common/', include('ModuleCommon.urls', namespace='ModuleCommon')),
# ]
#


