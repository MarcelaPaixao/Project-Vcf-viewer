# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class FltrdCybersegChr21Variantes(models.Model):
    # muitas linhas! verificar se representa problemapelofato deestar como inteiro!!!!!!
    id_variante = models.IntegerField(db_column='ID_VARIANTE', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    chrom = models.TextField(db_column='CHROM', blank=True, null=True)  # Field name made lowercase.
    pos = models.TextField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase.
    alt = models.TextField(db_column='ALT', blank=True, null=True)  # Field name made lowercase.
    # qual = models.TextField(db_column='QUAL', blank=True, null=True)  # Field name made lowercase.
    qual = models.FloatField(db_column='QUAL', blank=True, null=True)  # Field name made lowercase.
    filter = models.TextField(db_column='FILTER', blank=True, null=True)  # Field name made lowercase.
    info_dp = models.TextField(db_column='INFO_DP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fltrd_Cyberseg_chr21_Variantes'


class FltrdCybersegChr21Amostras(models.Model):
    # id_variante = models.IntegerField(db_column='ID_VARIANTE', blank=True, null=True)  # Field name made lowercase.
    id_variante = models.ForeignKey(FltrdCybersegChr21Variantes, models.DO_NOTHING, db_column='ID_VARIANTE', blank=True, null=True)  # Field name made lowercase.
    amostra = models.TextField(db_column='AMOSTRA', blank=True, null=True)  # Field name made lowercase.
    gt = models.TextField(db_column='GT', blank=True, null=True)  # Field name made lowercase.
    af = models.FloatField(db_column='AF', blank=True, null=True)  # Field name made lowercase.
    dp = models.FloatField(db_column='DP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fltrd_Cyberseg_chr21_Amostras'

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_time = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'
