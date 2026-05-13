from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin_tools/', include('admin_tools.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
