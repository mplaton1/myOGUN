from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^browse', views.browse, name='browse'),
    url(r'', views.search, name='search'),
]