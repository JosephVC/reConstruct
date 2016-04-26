from django.conf.urls import include, urls
from django.contrib import admin

urlpatterns = [
				url(r'^userprofiles/', include('userprofiles.urls')),
				url(r'^admin/', admin.site.urls),
]