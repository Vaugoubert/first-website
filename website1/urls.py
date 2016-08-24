"""website1 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'vaugoubert.views.home', name='home'),
    url(r'^home_page2', 'vaugoubert.views.home_page2', name='home_page2'),
    url(r'^chateau', 'vaugoubert.views.chateau', name='chateau'),
    url(r'^boulot', 'vaugoubert.views.boulot', name='boulot'),
    url(r'^repos', 'vaugoubert.views.repos', name='repos'),
    url(r'^histoire', 'vaugoubert.views.histoire', name='histoire'),
    url(r'^detente', 'vaugoubert.views.detente', name='detente'),
]
