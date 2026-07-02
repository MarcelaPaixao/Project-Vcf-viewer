from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import FltrdCybersegChr21Amostras, FltrdCybersegChr21Variantes
from django.contrib.auth.decorators import login_required
from .filters import VarianteFilter, AmostraFilter

def variantes(request):
    queryset = FltrdCybersegChr21Variantes.objects.all()

    f = VarianteFilter(request.GET, queryset=queryset)
    
    paginator = Paginator(f.qs, 85) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Cria uma cópia da URL atual (request.GET)
    query_params = request.GET.copy()
    
    # Remove a páginação da cópia, se ela existir, para não duplicar
    if 'page' in query_params:
        del query_params['page']

    context = {
        "filter": f,
        "vcf_data": page_obj,
        # O urlencode transforma o dicionário em texto de URL (ex: "chrom=chr1&qual=50")
        "query_params": query_params.urlencode(), 
    }

    return render(request, "vcf_viewer/variantes.html", context)

# @login_required
def amostras(request):
    queryset = FltrdCybersegChr21Amostras.objects.filter(nivel_sigilo=1)
    
    if request.user.is_staff:
        queryset = FltrdCybersegChr21Amostras.objects.all()

    f = AmostraFilter(request.GET, queryset=queryset)
    
    paginator = Paginator(f.qs, 85) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()

    if 'page' in query_params:
        del query_params['page']

    context = {
        "filter": f,
        "vcf_data": page_obj,
        "query_params" : query_params.urlencode()
    }
        
    return render(request, 'vcf_viewer/amostras.html', context)

# @login_required
def variante_detalhes(request, id_variante):
    variante = get_object_or_404(FltrdCybersegChr21Variantes, pk=id_variante)
    amostras = FltrdCybersegChr21Amostras.objects.filter(id_variante=id_variante, nivel_sigilo=1)
    
    if request.user.is_staff:
        amostras = FltrdCybersegChr21Amostras.objects.filter(id_variante=id_variante)
        # amostras = variante.objects.all() #poderia fazer assim?

    paginator = Paginator(amostras, 85) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    query_params = request.GET.copy()
    
    if 'page' in query_params:
        del query_params['page']
    
    context = {
        "variante": variante,
        "amostras": page_obj,
        "query_params": query_params.urlencode()
    }

    return render(request, 'vcf_viewer/variante_detalhes.html', context)

def home(request):
    return render(request, 'home.html')