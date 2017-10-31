
from django.conf.urls import url
from django.contrib import admin

from main.views import TwitterAnalyticsDashboard, Stackoverflow

urlpatterns = [
    url(r'^twitter/(?P<username>[\w-]+)/$', TwitterAnalyticsDashboard.as_view(), name='twitter_dashbaord'),
    url(r'^stackoverflow/$', Stackoverflow.as_view(), name='stackoverflow'),
]
