import django_filters
from .models import *

class VarianteFilter(django_filters.FilterSet):
    class Meta:
        model = FltrdCybersegChr21Variantes
        fields =  ['id_variante', 'chrom', 'pos', 'ref', 'alt', 'qual', 'filter', 'info_dp']

        # Caso queira fltros mais personalizados:
        # Passar um dicionário se quiser especificar o tipo exato de busca para cada coluna
        # fields = {
        #     'chrom': ['exact', 'icontains'], # Gera busca exata e busca parcial
        #     'pos': ['exact', 'gte', 'lte'],  # Gera busca exata, maior ou igual, e menor ou igual
        # } [4]