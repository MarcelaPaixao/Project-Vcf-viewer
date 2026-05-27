from django import forms
import django_filters
from .models import *

#non_empty do filter deve ser o pass ao invés de null

class VarianteFilter(django_filters.FilterSet):
    def filter_not_null(self, queryset, name, value):
        # Só aplica o filtro se a caixa estiver marcada (value == True)
        if value:
            # Filtra o banco para trazer apenas onde o campo não é nulo
            return queryset.filter(**{f"{name}__isnull": False})
        # Se a caixa não estiver marcada, devolve a tabela inteira sem filtrar
        return queryset

    id_var__notnull = django_filters.BooleanFilter(
        field_name='id_variante', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    id_var__exact = django_filters.NumberFilter(field_name='id_variante', lookup_expr='exact')

    chrom__notnull = django_filters.BooleanFilter(
        field_name='chrom', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    chrom__exact = django_filters.CharFilter(field_name='chrom', lookup_expr='exact')

    pos__notnull = django_filters.BooleanFilter(
        field_name='pos', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    pos__exact = django_filters.NumberFilter(field_name='pos', lookup_expr='exact')
    
    ref__notnull = django_filters.BooleanFilter(
        field_name='ref', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    ref__exact = django_filters.CharFilter(field_name='ref', lookup_expr='exact')

    alt__notnull = django_filters.BooleanFilter(
        field_name='alt', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    alt__exact = django_filters.CharFilter(field_name='alt', lookup_expr='exact')

    qual__gte = django_filters.NumberFilter(field_name='qual', lookup_expr='gte')
    qual__notnull = django_filters.BooleanFilter(
        field_name='qual', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    qual__exact = django_filters.NumberFilter(field_name='qual', lookup_expr='exact')

    filter__notnull = django_filters.BooleanFilter(
        field_name='filter', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    filter__exact = django_filters.CharFilter(field_name='filter', lookup_expr='exact')

    info_dp__notnull = django_filters.BooleanFilter(
        field_name='info_dp', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    info_dp__exact = django_filters.CharFilter(field_name='info_dp', lookup_expr='exact')

    info_gt__notnull = django_filters.BooleanFilter(
        field_name='info_gt', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    info_gt__exact = django_filters.CharFilter(field_name='info_gt', lookup_expr='exact')


    class Meta:
        model = FltrdCybersegChr21Variantes
        fields =  ['id_variante', 'chrom', 'pos', 'ref', 'alt', 'qual', 'filter', 'info_dp', 'info_gt']

        filter_overrides = {
            models.TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr' : 'icontains',
                },
            },
            models.IntegerField: {
                'filter_class': django_filters.NumberFilter,
                'extra': lambda f: {
                    'lookup_expr' : 'icontains',
                },
            },
            models.FloatField: {
                'filter_class': django_filters.NumberFilter,
                'extra': lambda f: {
                    'lookup_expr' : 'icontains',
                },
            },
        }