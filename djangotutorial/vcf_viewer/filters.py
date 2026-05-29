from django import forms
import django_filters
from .models import *
from django.db.models import Q

class VarianteFilter(django_filters.FilterSet):
    def filter_not_null(self, queryset, name, value):
        # Só aplica o filtro se a caixa estiver marcada (value == True)
        if value:
            lookup = '__'.join([name, 'isnull'])
            return queryset.filter(**{lookup:False})
        return queryset
    
    def filter_not_pass(self, queryset, name, value):
        if value:
            lookup_null_word = '__'.join([name, 'exact'])
            lookup = '__'.join([name, 'isnull'])
            return queryset.exclude(
                Q(**{lookup:True}) |  Q(**{lookup_null_word: "PASS"})
            )
        return queryset
    
    def filter_exact_toggle(self, queryset, name, value):
        if value:
            search_term = self.data.get(name)
            if search_term:
                lookup = '__'.join([name, 'exact'])
                return queryset.filter(**{lookup:search_term})
        return queryset

    # id_var__notnull = django_filters.BooleanFilter(
    #     field_name='id_variante', 
    #     method='filter_not_null', 
    #     widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    # )

    # id_var__exact = django_filters.BooleanFilter(
    #     field_name='id_variante', 
    #     method='filter_exact_toggle', 
    #     widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    # )

    chrom__notnull = django_filters.BooleanFilter(
        field_name='chrom', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    chrom__exact = django_filters.BooleanFilter(
        field_name='chrom', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    pos__notnull = django_filters.BooleanFilter(
        field_name='pos', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    pos__exact = django_filters.BooleanFilter(
        field_name='pos', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    ref__notnull = django_filters.BooleanFilter(
        field_name='ref', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    ref__exact = django_filters.BooleanFilter(
        field_name='ref', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    alt__notnull = django_filters.BooleanFilter(
        field_name='alt', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    alt__exact = django_filters.BooleanFilter(
        field_name='alt', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    qual__gte = django_filters.NumberFilter(field_name='qual', lookup_expr='gte') ###########################OLHAR!!!
    qual__notnull = django_filters.BooleanFilter(
        field_name='qual', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    qual__exact = django_filters.BooleanFilter(
        field_name='qual', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    filter__notnull = django_filters.BooleanFilter(
        field_name='filter', 
        # method='filter_not_null',
        method='filter_not_pass',
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    filter__exact = django_filters.BooleanFilter(
        field_name='filter', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    info_dp__notnull = django_filters.BooleanFilter(
        field_name='info_dp', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    info_db__exact = django_filters.BooleanFilter(
        field_name='info_db', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )

    info_gt__notnull = django_filters.BooleanFilter(
        field_name='info_gt', 
        method='filter_not_null', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )
    
    info_gt__exact = django_filters.BooleanFilter(
        field_name='info_gt', 
        method='filter_exact_toggle', 
        widget=forms.CheckboxInput(attrs={'class': 'hidden-checkbox'})
    )


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