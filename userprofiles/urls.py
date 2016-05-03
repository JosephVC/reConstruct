from django.conf.urls import url

from userprofiles.views import home_view, profile_view, create_project_view

urlpatterns = [
    url(r'^$',
        home_view,
        name="home"),
	url(r'^profile/$',
        profile_view,
        name="profile"),
    url(r'^new-project/$',
        create_project_view,
        name="create_project"),
]