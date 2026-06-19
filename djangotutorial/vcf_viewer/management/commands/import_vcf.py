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
        df_variantes.columns = [
            f"{col[0]}_{col[1]}" if col[1] else col[0] 
            for col in df_variantes.columns
        ]
        df_variantes.insert(0, 'ID_VARIANTE', range(1, len(df_variantes) + 1))
        
        
        # Tabela de amostras
        df_amostras = df_input.iloc[:, 8:].copy()
        df_amostras = df_amostras.stack(level=0, future_stack=True).reset_index()
        df_amostras = df_amostras.rename(columns={'level_0': 'ID_VARIANTE', 'level_1': 'AMOSTRA'})
        df_amostras['ID_VARIANTE'] = df_amostras['ID_VARIANTE'] + 1

        if 'GT' in df_amostras.columns:
            # Transforma a lista em texto, mas se o dado for vazio (None), mantém vazio.
            df_amostras['GT'] = df_amostras['GT'].apply(lambda x: str(x) if x is not None else None)
        
        # Adiciona coluna de nível de sigilo e define amostras sigilosas
        protected_samples = ['UFES_001', 'UFES_003', 'UFES_006', 'UFES_007']
        df_amostras['NIVEL_SIGILO'] = 1
        df_amostras.loc[df_amostras['AMOSTRA'].isin(protected_samples), 'NIVEL_SIGILO'] = 2

        # 4. Limpeza opcional (Descomente se quiser apagar os dados antigos a cada importação)
        # FltrdCybersegChr21Variantes.objects.all().delete()
        # FltrdCybersegChr21Amostras.objects.all().delete()

        FltrdCybersegChr21Variantes.objects.bulk_create([
            FltrdCybersegChr21Variantes(
                id_variante=row['ID_VARIANTE'],
                chrom=row['CHROM'],
                pos=row['POS'],
                ref=row['REF'],
                alt=row['ALT'],
                qual=row['QUAL'],
                filter=row['FILTER'],
                info_dp=row['INFO_DP'],
                info_gt=row['INFO_GT'],
            ) for _,row in df_variantes.iterrows()
        ])

        FltrdCybersegChr21Amostras.objects.bulk_create([
            FltrdCybersegChr21Amostras(
                id_variante_id=row['ID_VARIANTE'],
                amostra=row['AMOSTRA'],
                gt=row['GT'],
                af=row['AF'],
                dp=row['DP'],
                nivel_sigilo=row['NIVEL_SIGILO']
            ) for _,row in df_amostras.iterrows()
        ])

        self.stdout.write(self.style.SUCCESS('Importação finalizada com sucesso!'))