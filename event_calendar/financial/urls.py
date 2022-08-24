from django.urls import path

from . import views

app_name = "financial"


urlpatterns = [
    path("financial/", views.financial.as_view(), name="financial"),
]
