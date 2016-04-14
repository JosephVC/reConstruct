from django.contrib import admin
from wasteprocessors.models import UserType, Profile, ProjectType, Project, MaterialType, Material, WasteType, Waste, WasteProcessor

# Register your models here.

admin.site.register(UserType)
admin.site.register(Profile)
admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(MaterialType)
admin.site.register(Material)
admin.site.register(WasteType)
admin.site.register(Waste)
admin.site.register(WasteProcessor)

