from django.urls import path
from . import views

app_name = 'vcf_viewer'

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("variantes", views.variantes, name="variantes"),
    path("amostras", views.amostras, name="amostras"),
    path("variantes/<int:id_variante>/", views.variante_detalhes, name="variante_detalhes"),
]