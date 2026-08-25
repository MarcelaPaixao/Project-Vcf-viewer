# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FltrdCybersegChr21Variantes(models.Model):
    # id_variante = models.IntegerField(db_column='ID_VARIANTE', blank=True, null=True)  # Field name made lowercase.
    id_variante = models.IntegerField(db_column='ID_VARIANTE', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    chrom = models.TextField(db_column='CHROM', blank=True, null=True)  # Field name made lowercase.
    pos = models.IntegerField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase.
    alt = models.TextField(db_column='ALT', blank=True, null=True)  # Field name made lowercase.
    qual = models.DecimalField(db_column='QUAL', decimal_places=2, max_digits=10, blank=True, null=True)  # Field name made lowercase.
    filter = models.TextField(db_column='FILTER', blank=True, null=True)  # Field name made lowercase.
    info_dp = models.TextField(db_column='INFO_DP', blank=True, null=True)  # Field name made lowercase.
    info_gt = models.TextField(db_column='INFO_GT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Fltrd_Cyberseg_chr21_Variantes'

class FltrdCybersegChr21Amostras(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='rowid')

    id_variante = models.ForeignKey(FltrdCybersegChr21Variantes, on_delete=models.CASCADE, db_column='ID_VARIANTE')  # Field name made lowercase.
    amostra = models.TextField(db_column='AMOSTRA', blank=True, null=True)  # Field name made lowercase.
    gt = models.TextField(db_column='GT', blank=True, null=True)  # Field name made lowercase.
    af = models.FloatField(db_column='AF', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    
    nivel_sigilo = models.IntegerField(db_column='NIVEL_SIGILO', blank=True, null=True, default=1) 

    class Meta:
        managed = True
        db_table = 'Fltrd_Cyberseg_chr21_Amostras'
