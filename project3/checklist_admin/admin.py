from django.contrib import admin
from django.urls import include, path
from django.template.response import TemplateResponse

# Register your models here.
class ChecklistAdmin(admin.AdminSite):
    site_header = "Checklist Administration"
    def profile_view(self, request): 
        request.current_app = self.name
        context = self.each_context(request)
        return TemplateResponse(request, "admin_profile.html", context)
    def get_urls(self):
        urls = super().get_urls()
        url_patterns = [
            path("admin_profile", self.admin_view(self.profile_view))
        ]
        return url_patterns + urls
    

