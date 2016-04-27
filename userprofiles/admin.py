from django.contrib import admin
from userprofiles.models import UserType, Profile, ProjectType, Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"project_slug": ("project",)}

admin.site.register(UserType)
admin.site.register(Profile)
admin.site.register(ProjectType)
admin.site.register(Project, ProjectAdmin)
