from django.contrib import admin
from wasteprocessors.models import    MaterialType, Material, WasteType, WasteProcessor

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"project_slug": ("project",)}

class MaterialTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"material_slug": ("material_type",)}

admin.site.register(UserType)
admin.site.register(Profile)
admin.site.register(ProjectType)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MaterialType, MaterialTypeAdmin)
=======
#admin.site.register(UserType)
#admin.site.register(Profile)
#admin.site.register(ProjectType)
#admin.site.register(Project)
admin.site.register(MaterialType)
admin.site.register(Material)
admin.site.register(WasteType)
#admin.site.register(Waste)
admin.site.register(WasteProcessor)

