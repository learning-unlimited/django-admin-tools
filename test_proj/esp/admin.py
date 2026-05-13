# Stub so that admin_tools.utils.get_admin_site() can resolve
# `from esp.admin import admin_site` in the test project without
# the real ESP package installed.
from django.contrib import admin

admin_site = admin.site
