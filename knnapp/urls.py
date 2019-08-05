from django.conf.urls import url
from .views import FileView,LocationView
urlpatterns = [
  url(r'^upload/$', FileView.as_view(), name='file-upload'),
  url(r'^location/$', LocationView.as_view(), name='file-location'),
]