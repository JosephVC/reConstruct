from django.conf.urls import url

from wasteprocessors.views import salvage_companies_list, \
    material_search_view, material_search_results

urlpatterns = [
    url(r'^salvage-companies/$',
        salvage_companies_list,
        name="salvage_companies"),
    url(r'^project/(?P<project_slug>[-\w]+)/$',
        material_search_view,
        name="material_search"),
    url(r'^results/(?P<waste_id>\d+)/$',
        material_search_results,
        name="material_search_results"),
]