from django.conf.urls import url

from wasteprocessors.views import waste_processor_detail, material_search_view, material_search_results

urlpatterns = [
    url(r'^waste-processors/(?P<waste_processor_id>\d+)/$',
        waste_processor_detail,
        name="waste_processor_detail"),
    url(r'^project/(?P<project_id>\d+)/$',
        material_search_view,
        name="material_search"),
    url(r'^results/(?P<waste_id>\d+)/$',
        material_search_results,
        name="material_search_results"),
]