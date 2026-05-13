from django.urls import re_path
from admin_tools.menu import views

urlpatterns = [
    re_path(
        r'^add_bookmark/$',
        views.add_bookmark,
        name='admin-tools-menu-add-bookmark'
    ),
    re_path(
        r'^edit_bookmark/(?P<id>.+)/$',
        views.edit_bookmark,
        name='admin-tools-menu-edit-bookmark'
    ),
    re_path(
        r'^remove_bookmark/(?P<id>.+)/$',
        views.remove_bookmark,
        name='admin-tools-menu-remove-bookmark'
    ),
]
