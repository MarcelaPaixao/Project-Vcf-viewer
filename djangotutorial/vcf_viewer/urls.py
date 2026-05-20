from django.urls import path
from . import views

app_name = 'vcf_viewer'

urlpatterns = [
    path("", views.index, name="index"),
]