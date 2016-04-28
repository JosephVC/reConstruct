from django.conf.urls import url

from userprofiles.views import create_profile_view

urlpatterns = [
	url(r'^$',
        create_profile_view,
        name="create_profile"),
    url(r'^new-project/$',
        create_project_view,
        name="create_project"),
]