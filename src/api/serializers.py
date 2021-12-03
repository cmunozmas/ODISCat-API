# serializers.py
from rest_framework import serializers
from .models import Catalogue, CatalogueRelations, CatalogueContributedto, CatalogueDois, CatalogueM2Mtechnologies, CatalogueObtainedfrom, CatalogueRelations, CatalogueRelationsGoosEovs, CatalogueSeaRegions, CatalogueThemes, CatalogueTypes, DataSystems, Dois, GoosEovs, Institution, Keywords, M2Mtechnologies, Policies, SeaRegions, Standards, Themes, Types

class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'name', 'name_eng')

class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    abstract = serializers.CharField(source='ds_abstract')
    creation_date = serializers.CharField(source='entry_date')
    last_update = serializers.CharField(source='update_date')
    url = serializers.CharField(source='ds_url')
    parent_url = serializers.CharField(source='ds_parent_project_url')
    name = serializers.CharField(source='ds_name_english')
    name_original = serializers.CharField(source='ds_name_original')
    acronym = serializers.CharField(source='ds_acronym')
    citation = serializers.CharField(source='ds_citation')
    policy = serializers.CharField(source='md_policy.name')
    contributing_countries = serializers.CharField(source='ds_countries')
    site_owner_countries = serializers.CharField(source='ds_site_countries')
    #owner_institution = serializers.CharField(source='institution')
    institution = InstitutionSerializer()
    languages = serializers.CharField(source='ds_languages')
    odisarch_type = serializers.CharField(source='odis_arch_type')
    odisarch_url = serializers.CharField(source='odis_arch_url')
    class Meta:
        model = Catalogue
        fields = ('id', 'name', 'name_original', 'acronym', 'abstract', 'url', 'parent_url', 'policy', 'contributing_countries', 'site_owner_countries', 'citation', 'last_update', 'creation_date', 'institution', 'languages', 'odisarch_type', 'odisarch_url')

class CatalogueContributedtoSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    datasystems = serializers.CharField(source='datasystems.name')
    class Meta:
        model = CatalogueContributedto
        fields = ('catalogue', 'datasystems')

class CatalogueDoisSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    class Meta:
        model = CatalogueDois
        fields = ('catalogue', 'dois')

class CatalogueM2MtechnologiesSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    class Meta:
        model = CatalogueM2Mtechnologies
        fields = ('catalogue', 'm2mtechnologies')

class CatalogueObtainedfromSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    datasystems = serializers.CharField(source='datasystems.name')
    datasystems_id = serializers.IntegerField(source='datasystems.id')
    class Meta:
        model = CatalogueObtainedfrom
        fields = ('catalogue', 'datasystems', 'datasystems_id')

class CatalogueRelationsSerializer(serializers.ModelSerializer):
    obtainer = CatalogueSerializer()
    contributor = CatalogueSerializer()
    class Meta:
        model = CatalogueRelations
        fields = ('id','obtainer', 'contributor')

class GoosEovsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoosEovs
        fields = ('id', 'name')

class CatalogueRelationsGoosEovsSerializer(serializers.ModelSerializer):
    #catalogue_relations = CatalogueSerializer()
    goos_eovs = GoosEovsSerializer()

    class Meta:
        model = CatalogueRelationsGoosEovs
        fields = ('catalogue_relations', 'goos_eovs')

class CatalogueSeaRegionsSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    regionsid = serializers.CharField(source='sea_regions.name')
    class Meta:
        model = CatalogueSeaRegions
        fields = ('catalogue', 'regionsid')

class CatalogueThemesSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    themes = serializers.CharField(source='themes.name')
    class Meta:
        model = CatalogueThemes
        fields = ('catalogue', 'themes')

class CatalogueTypesSerializer(serializers.HyperlinkedModelSerializer):
    catalogue = CatalogueSerializer(required=True)
    types = serializers.CharField(source='types.name')
    class Meta:
        model = CatalogueTypes
        fields = ('catalogue', 'types')

class DataSystemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSystems
        fields = ('id', 'name', 'description')

class DoisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dois
        fields = ('name', 'description')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keywords
        fields = ('name', 'description')

class M2MtechnologiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = M2Mtechnologies
        fields = ('name', 'description')

class PoliciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policies
        fields = ('name', 'description', 'active')

class SeaRegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeaRegions
        fields = ('name', 'description', 'active')

class StandardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Standards
        fields = ('name', 'description')

class ThemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Themes
        fields = ('name', 'description')

class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
        fields = ('name', 'description')
