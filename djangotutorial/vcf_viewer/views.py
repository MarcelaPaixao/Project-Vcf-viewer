from django.shortcuts import render
from django.core.paginator import Paginator

from .models import FltrdCybersegChr21Amostras, FltrdCybersegChr21Variantes
from django.contrib.auth.decorators import login_required
from .filters import VarianteFilter, AmostraFilter

@login_required
def variantes(request):
    queryset = FltrdCybersegChr21Variantes.objects.all()

    f = VarianteFilter(request.GET, queryset=queryset)
    
    paginator = Paginator(f.qs, 100) 
    
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

@login_required
def amostras1(request):
    queryset = FltrdCybersegChr21Amostras.objects.all()
    
    paginator = Paginator(queryset, 100) 
    
    # Pega o número da página atual vindo da URL (ex: /amostras?page=2)
    page_number = request.GET.get('page')
    
    vcf_data = paginator.get_page(page_number)
    
    return render(request, 'vcf_viewer/amostras.html', {'vcf_data': vcf_data})

@login_required
def amostras(request):
    queryset = FltrdCybersegChr21Amostras.objects.all()

    f = AmostraFilter(request.GET, queryset=queryset)
    
    paginator = Paginator(f.qs, 100) 
    
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

@login_required
def home(request):
    return render(request, 'home.html')

    # fazer um para o id davariante associado ever de transforma em um linkpara direcionar para outra página 
    # que vai ter todas as infos sobre essa variante especifica e as amostras relacionadas a ela