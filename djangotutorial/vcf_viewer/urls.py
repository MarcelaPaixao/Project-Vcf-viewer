from django.urls import path
from . import views

app_name = 'vcf_viewer'

urlpatterns = [
    path("variantes", views.variantes, name="variantes"),
    path("amostras", views.amostras, name="amostras"),
]