"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.views import login, logout
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^favicon\.ico$', 
        RedirectView.as_view(url=settings.MEDIA_URL + 
            'Path_to_favicon_file')),
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^', include('myblog.urls')),
    url(r'^', include('wasteprocessors.urls')),
    url(r'^favicon\.ico$', 
        RedirectView.as_view(url=settings.MEDIA_URL + 
            '../static/favicon.ico')),
    url(r'^login/$',
        login,
        {'template_name': 'login.html'},
        name="login"),
    url(r'^logout/$',
        logout,
        {'next_page': '/'},
        name="logout"),
]
