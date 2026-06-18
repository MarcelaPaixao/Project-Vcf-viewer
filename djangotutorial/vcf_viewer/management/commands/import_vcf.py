from django.core.management.base import BaseCommand
from vcf_viewer.models import FltrdCybersegChr21Variantes, FltrdCybersegChr21Amostras
from cyvcf2 import VCF
import  pandas as pd
import numpy as np
from enum import Enum

def vcf_to_df_filtered_Samples(vcf_path):
    vcf_file = VCF(vcf_path)
    #Define as colunas desejadas e define subcolunas para pegar apenas parte de INFO
    cols_tuples = [
        ('CHROM', ''),
        ('POS', ''),
        ('REF', ''),
        ('ALT', ''),
        ('QUAL', ''),
        ('FILTER', ''),
        ('INFO', 'DP'),  
        ('INFO', 'GT'),  
    ]

    #Acrescenta as colunas de amostras
    for sample in vcf_file.samples:
        sample_tuple = [
            (sample, 'GT'),
            (sample, 'AF'),
            (sample, 'DP'),
        ]
        cols_tuples.extend(sample_tuple)

    multi_cols = pd.MultiIndex.from_tuples(cols_tuples)

    data = []
    for variant in vcf_file:
        fltrd_line = [
            variant.CHROM,
            variant.POS,                                   
            variant.REF,
            ",".join(variant.ALT) if variant.ALT else ".",  # ALT é uma lista, transformamos em string separada por vírgula
            variant.QUAL,                                   
            variant.FILTER if variant.FILTER else "PASS",   # cyvcf2 retorna None se for PASS
            variant.INFO.get('DP'),                        
            variant.INFO.get('GT'),    
        ]

        # Extração com cyvcf2. Retorna arrays ou None.
        genotypes = variant.genotypes # array com os GT's
        af_array = variant.format('AF')
        dp_array = variant.format('DP')

        samples_fltrd_line = []
        for i in range(len(vcf_file.samples)):
            # Trocamos o "." por None. Isso permite que o Pandas use NaN e mantenha a coluna numérica!
            samples_fltrd_line.extend([
                genotypes[i] if genotypes is not None else None,
                af_array[i][0] if af_array is not None else None,
                dp_array[i][0] if dp_array is not None else None
            ])
        
        # Une as amostras ao restante das informações
        fltrd_line.extend(samples_fltrd_line)
        data.append(fltrd_line)
    
    df = pd.DataFrame(data, columns=multi_cols)
    vcf_file.close()
    return df

class Command(BaseCommand):
    help = "Processa um  arquivo VCF e carrega em um banco de dados"

    def  add_arguments(self, parser):
        parser.add_argument('path_vcf', type=str, help="Caminho para arquivo .vcf")

    def handle(self, *args, **kwargs):
        file_path = kwargs['path_vcf']

        df_input = vcf_to_df_filtered_Samples(file_path)

        # Tabela de variantes
        df_variantes = df_input.iloc[:, :8].copy()
        # Tabela de amostras
        df_amostras = df_input.iloc[:, 8:].copy()

        # df_amostras = df_amostras.stack(level=0, future_stack=True).reset_index()

        self.stdout.write(self.style.SUCCESS, 'Importação finalizada com sucesso!')