# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogue(models.Model):
    submitter_role_id = models.ForeignKey('Roles', models.DO_NOTHING)
    md_policy = models.ForeignKey('Policies', models.DO_NOTHING)
    submitter_oe_id = models.IntegerField()
    entry_date = models.DateTimeField()
    update_date = models.DateTimeField(blank=True, null=True)
    ds_url = models.CharField(max_length=255)
    ds_parent_project_url = models.CharField(max_length=255, blank=True, null=True)
    ds_project_end_date = models.DateTimeField(blank=True, null=True)
    ds_name_english = models.CharField(max_length=255)
    ds_name_original = models.CharField(max_length=255, blank=True, null=True)
    ds_acronym = models.CharField(max_length=255, blank=True, null=True)
    ds_abstract = models.TextField()
    ds_citation = models.TextField()
    ds_contact_name = models.CharField(max_length=255, blank=True, null=True)
    ds_contact_email = models.CharField(max_length=255, blank=True, null=True)
    ds_tech_contact_email = models.CharField(max_length=255)
    ds_languages = models.TextField()
    ds_countries = models.TextField()
    ds_tech_notes = models.TextField(blank=True, null=True)
    md_spatial_coverage = models.TextField(blank=True, null=True)
    ds_site_countries = models.TextField(blank=True, null=True)
    is_live = models.IntegerField(blank=True, null=True)
    is_live_date = models.DateTimeField(blank=True, null=True)
    institution = models.ForeignKey('Institution', models.DO_NOTHING, blank=True, null=True)
    odis_arch_type = models.ForeignKey('OdisArchType', models.DO_NOTHING, blank=True, null=True)
    odis_arch_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue'


class CatalogueCatalogue(models.Model):
    catalogue_source = models.OneToOneField(Catalogue, models.DO_NOTHING, db_column='catalogue_source', primary_key=True, related_name='catalogue_source')
    catalogue_target = models.ForeignKey(Catalogue, models.DO_NOTHING, db_column='catalogue_target', related_name='catalogue_target')

    class Meta:
        managed = False
        db_table = 'catalogue_catalogue'
        unique_together = (('catalogue_source', 'catalogue_target'),)


class CatalogueContributedto(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    datasystems = models.ForeignKey('DataSystems', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_contributedto'
        unique_together = (('catalogue', 'datasystems'),)


class CatalogueDois(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    dois = models.ForeignKey('Dois', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_dois'
        unique_together = (('catalogue', 'dois'),)


class CatalogueKeywords(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    keywords = models.ForeignKey('Keywords', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_keywords'
        unique_together = (('catalogue', 'keywords'),)


class CatalogueM2Mtechnologies(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    m2mtechnologies = models.ForeignKey('M2Mtechnologies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_m2mtechnologies'
        unique_together = (('catalogue', 'm2mtechnologies'),)


class CatalogueObtainedfrom(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    datasystems = models.ForeignKey('DataSystems', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_obtainedfrom'
        unique_together = (('catalogue', 'datasystems'),)


class CatalogueRelations(models.Model):
    contributor = models.ForeignKey(Catalogue, models.DO_NOTHING, blank=True, null=True, related_name='contributor')
    obtainer = models.ForeignKey(Catalogue, models.DO_NOTHING, blank=True, null=True, related_name='obtainer')

    class Meta:
        managed = False
        db_table = 'catalogue_relations'


class CatalogueRelationsGoosEovs(models.Model):
    catalogue_relations = models.OneToOneField(CatalogueRelations, models.DO_NOTHING, primary_key=True)
    goos_eovs = models.ForeignKey('GoosEovs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_relations_goos_eovs'
        unique_together = (('catalogue_relations', 'goos_eovs'),)


class CatalogueSeaRegions(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    sea_regions = models.ForeignKey('SeaRegions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_sea_regions'
        unique_together = (('catalogue', 'sea_regions'),)


class CatalogueStandard(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    standard = models.ForeignKey('Standards', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_standard'
        unique_together = (('catalogue', 'standard'),)


class CatalogueThemes(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    themes = models.ForeignKey('Themes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_themes'
        unique_together = (('catalogue', 'themes'),)


class CatalogueTypes(models.Model):
    catalogue = models.OneToOneField(Catalogue, models.DO_NOTHING, primary_key=True)
    types = models.ForeignKey('Types', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_types'
        unique_together = (('catalogue', 'types'),)


class DataSystems(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_systems'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DoctrineMigrationVersions(models.Model):
    version = models.CharField(primary_key=True, max_length=191)
    executed_at = models.DateTimeField(blank=True, null=True)
    execution_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctrine_migration_versions'


class Dois(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dois'


class GoosEovs(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'goos_eovs'


class Institution(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    name_eng = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution'


class Keywords(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keywords'


class M2Mtechnologies(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm2mtechnologies'


class OdisArchType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'odis_arch_type'


class Policies(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'policies'


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles'


class SeaRegions(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sea_regions'


class Standards(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'standards'


class Themes(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'themes'


class Types(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'types'
