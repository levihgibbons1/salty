from django.urls import path

from salty.views import health, home

urlpatterns = [path("", home), path("health/", health)]
