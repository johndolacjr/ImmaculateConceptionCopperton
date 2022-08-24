from django.urls import path

from . import views

app_name = "history"


urlpatterns = [
    path("history/", views.history.as_view(), name="history"),
]
