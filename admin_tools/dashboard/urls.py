from django.urls import re_path

from admin_tools.dashboard import views

urlpatterns = [
    re_path(
        r'^set_preferences/(?P<dashboard_id>.+)/$',
        views.set_preferences,
        name='admin-tools-dashboard-set-preferences'
    ),
]
