from django.conf.urls import url

from userprofiles.views import profile_view

urlpatterns = [
	url(r'^$',
        profile_view,
        name="profile"),
]