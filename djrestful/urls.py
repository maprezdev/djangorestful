# This file defines the root URL configurations, and therefore we must include
# the URL patterns declared in the previously coded toys/urls.py file
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('toys.urls')),
]
