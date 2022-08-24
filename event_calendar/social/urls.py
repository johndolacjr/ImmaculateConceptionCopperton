from django.urls import path

from . import views

app_name = "social"


urlpatterns = [
    path("social/", views.social.as_view(), name="social"),
]
