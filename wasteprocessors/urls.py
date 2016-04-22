from django.conf.urls import url

from wasteprocessors.views import salvage_companies_list, material_search_view

urlpatterns = [
    url(r'^$',
        salvage_companies_list,
        name="salvage_companies"),
    url(r'^material-search/$',
        material_search_view,
        name="material_search"),
]