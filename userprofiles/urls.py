from django.conf.urls import url

from userprofiles.views import home_view, profile_view, edit_profile_view, create_project_view

urlpatterns = [
    url(r'^$',
        home_view,
        name="home"),
	url(r'^profile/$',
        profile_view,
        name="profile"),
    url(r'^profile/edit/$',
        edit_profile_view,
        name="edit_profile"),
    url(r'^new-project/$',
        create_project_view,
        name="new_project"),
]