from django.conf.urls import url

from wasteprocessors.views import index, salvage_companies_list, material_search_view, material_search_results

urlpatterns = [
    url(r'^$',
        index,
        name="index"),
    url(r'^salvage-companies/$',
        salvage_companies_list,
        name="salvage_companies"),
    url(r'^material-search/$',
        material_search_view,
        name="material_search"),
    url(r'^material-search/(?P<project_slug>[-\w]+)/(?P<material_slug>[-\w]+)/$',
        material_search_results,
        name="material_search_results"),
]