from django.urls import path

from . import views

app_name = "calendar2"


urlpatterns = [
    path("calendar2/", views.calendar2, name="calendar2"),
]
