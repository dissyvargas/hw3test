from django.contrib.admin.apps import AdminConfig

class ChecklistAdminConfig(AdminConfig):
    default_site = 'checklist_admin.admin.ChecklistAdmin'