from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    site_header = "Sistema bancário"

admin_site = CustomAdminSite()