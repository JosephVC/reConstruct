from django.contrib import admin
from wasteprocessors.models import MaterialType, Waste, WasteType, WasteProcessor

class MaterialTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"material_slug": ("material_type",)}

admin.site.register(MaterialType, MaterialTypeAdmin)
admin.site.register(WasteType)
admin.site.register(Waste)
admin.site.register(WasteProcessor)

