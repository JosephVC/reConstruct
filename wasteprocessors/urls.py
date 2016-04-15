from django.conf.urls import url

from wasteprocessors.views import salvage_companies_list

urlpatterns = [
    url(r'^$',
        salvage_companies_list,
        name="salvage_companies"),
]