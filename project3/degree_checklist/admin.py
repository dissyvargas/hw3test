from django.contrib import admin
from degree_checklist.models import (Degree, requiredCourses, degreeSpecific)

# Register your models here.
admin.site.register(Degree)
admin.site.register(requiredCourses)
admin.site.register(degreeSpecific)
