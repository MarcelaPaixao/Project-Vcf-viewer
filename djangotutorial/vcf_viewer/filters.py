import django_filters
from .models import *

class VarianteFilter(django_filters.FilterSet):
    qual = django_filters.NumberFilter(field_name='qual', lookup_expr='gt', label='Qual gte')
    class Meta:
        model = FltrdCybersegChr21Variantes
        fields =  ['id_variante', 'chrom', 'pos', 'ref', 'alt', 'filter', 'info_dp']

        filter_overrides = {
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr' : 'icontains',
                },
            },
        }
