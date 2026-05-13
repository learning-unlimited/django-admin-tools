from django.conf import settings
from django.urls import include, re_path

urlpatterns = []
if 'admin_tools.menu' in settings.INSTALLED_APPS:
    urlpatterns.append(re_path(r'^menu/', include('admin_tools.menu.urls')))
if 'admin_tools.dashboard' in settings.INSTALLED_APPS:
    urlpatterns.append(
        re_path(r'^dashboard/', include('admin_tools.dashboard.urls'))
    )
