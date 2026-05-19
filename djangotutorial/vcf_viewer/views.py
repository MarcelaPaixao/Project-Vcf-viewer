from django.shortcuts import render
# from django.http import HttpResponse
from .models import FltrdCybersegChr21Amostras, FltrdCybersegChr21Variantes

# def index(request):
#     return HttpResponse("Hello. You're at the vcf_viewer index.")

def index(request):
    # Recupera todos os registros do banco de dados
    amostras_data = FltrdCybersegChr21Amostras.objects.all()
    variantes_data = FltrdCybersegChr21Variantes.objects.all()
    vcf_data = FltrdCybersegChr21Variantes.objects.all()

    # Passa os dados recuperados para o template
    # context = {
    #     "amostras_data": amostras_data,
    #     "variantes_data": variantes_data
    # }
    context = {
        "vcf_data": vcf_data
    }

    return render(request, "vcf_viewer/index.html", context)