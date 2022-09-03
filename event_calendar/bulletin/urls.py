from django.urls import path

from . import views

app_name = "bulletin"


urlpatterns = [
    path("bulletin/", views.bulletin, name="bulletin"),
]
