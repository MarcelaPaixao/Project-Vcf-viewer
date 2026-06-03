from django.shortcuts import render
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import FltrdCybersegChr21Amostras, FltrdCybersegChr21Variantes
from django.contrib.auth.decorators import login_required
from .filters import VarianteFilter

@login_required
def variantes(request):
    # Recupera todos os registros do banco de dados
    # amostras_data = FltrdCybersegChr21Amostras.objects.all()
    # variantes_data = FltrdCybersegChr21Variantes.objects.all()
    
    # Passa os dados recuperados para o template
    # context = {
    #     "amostras_data": amostras_data,
    #     "variantes_data": variantes_data
    # }
    
    # vcf_data = FltrdCybersegChr21Variantes.objects.all()
    # context = {"vcf_data": vcf_data}
    # return render(request, "vcf_viewer/variantes.html", context)

    f = VarianteFilter(request.GET, queryset=FltrdCybersegChr21Variantes.objects.all())
    context = {"filter": f}

    return render(request, "vcf_viewer/variantes.html", context)

@login_required
def amostras(request):
    # Obtém todos os registros
    queryset = FltrdCybersegChr21Amostras.objects.all()
    
    # Define o limite de registros por página (ex: 100 por tela)
    paginator = Paginator(queryset, 100) 
    
    # Pega o número da página atual vindo da URL (ex: /amostras?page=2)
    page_number = request.GET.get('page')
    
    # Extrai apenas as 100 linhas correspondentes àquela página
    vcf_data = paginator.get_page(page_number)
    
    return render(request, 'pag_amostras.html', {'vcf_data': vcf_data})