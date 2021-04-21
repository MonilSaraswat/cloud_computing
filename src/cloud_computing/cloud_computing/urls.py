from django.conf.urls import include, url
from django.contrib import admin

from buttons_screen.views import ButtonScreen, upload_file_to_aws, MetaDataScreen

urlpatterns = [
    # Examples:
    url(r'^$', ButtonScreen.as_view(), name='ButtonScreen'),
    url(r'^upload_image_to_aws/', upload_file_to_aws),
    url(r'^images/(?P<image_id>\d+)/$', MetaDataScreen.as_view()),
]
