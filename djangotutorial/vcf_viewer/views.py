from django.shortcuts import render
from .models import FltrdCybersegChr21Amostras, FltrdCybersegChr21Variantes
from django.contrib.auth.decorators import login_required
from .filters import VarianteFilter

@login_required
def index(request):
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
    # return render(request, "vcf_viewer/index.html", context)

    f = VarianteFilter(request.GET, queryset=FltrdCybersegChr21Variantes.objects.all())
    context = {"filter": f}

    return render(request, "vcf_viewer/index.html", context)