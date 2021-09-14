# views.py

import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CatalogueSerializer, CatalogueRelationsSerializer, CatalogueContributedtoSerializer, CatalogueDoisSerializer, CatalogueM2MtechnologiesSerializer, CatalogueObtainedfromSerializer, CatalogueSeaRegionsSerializer, CatalogueThemesSerializer, CatalogueTypesSerializer, DataSystemsSerializer, DoisSerializer, KeywordsSerializer, M2MtechnologiesSerializer, PoliciesSerializer, SeaRegionsSerializer, StandardsSerializer, ThemesSerializer, TypesSerializer
from .models import Catalogue, CatalogueRelations, CatalogueContributedto, CatalogueDois, CatalogueM2Mtechnologies, CatalogueObtainedfrom, CatalogueSeaRegions, CatalogueThemes, CatalogueTypes, DataSystems, Dois, Keywords, M2Mtechnologies, Policies, SeaRegions, Standards, Themes, Types



class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['md_policy', 'ds_countries']

class CatalogueRelationsViewSet(viewsets.ModelViewSet):
    queryset = CatalogueRelations.objects.all()
    serializer_class = CatalogueRelationsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue', 'contributor']

class CatalogueContributedtoViewSet(viewsets.ModelViewSet):
    queryset = CatalogueContributedto.objects.all()
    serializer_class = CatalogueContributedtoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue', 'datasystems']

class CatalogueDoisViewSet(viewsets.ModelViewSet):
    queryset = CatalogueDois.objects.all()
    serializer_class = CatalogueDoisSerializer

class CatalogueM2MtechnologiesViewSet(viewsets.ModelViewSet):
    queryset = CatalogueM2Mtechnologies.objects.all()
    serializer_class = CatalogueM2MtechnologiesSerializer

class CatalogueObtainedfromViewSet(viewsets.ModelViewSet):
    queryset = CatalogueObtainedfrom.objects.all()
    serializer_class = CatalogueObtainedfromSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue', 'datasystems']

class CatalogueSeaRegionsViewSet(viewsets.ModelViewSet):
    queryset = CatalogueSeaRegions.objects.all()
    serializer_class = CatalogueSeaRegionsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue_id', 'sea_regions_id']

class CatalogueThemesViewSet(viewsets.ModelViewSet):
    queryset = CatalogueThemes.objects.all()
    serializer_class = CatalogueThemesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue_id', 'themes_id']

class CatalogueTypesViewSet(viewsets.ModelViewSet):
    queryset = CatalogueTypes.objects.all()
    serializer_class = CatalogueTypesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['catalogue_id', 'types_id']

class DataSystemsViewSet(viewsets.ModelViewSet):
    queryset = DataSystems.objects.all()
    serializer_class = DataSystemsSerializer

class DoisViewSet(viewsets.ModelViewSet):
    queryset = Dois.objects.all().order_by('name')
    serializer_class = DoisSerializer

class KeywordsViewSet(viewsets.ModelViewSet):
    queryset = Keywords.objects.all().order_by('name')
    serializer_class = KeywordsSerializer

class M2MtechnologiesViewSet(viewsets.ModelViewSet):
    queryset = M2Mtechnologies.objects.all().order_by('name')
    serializer_class = M2MtechnologiesSerializer

class PoliciesViewSet(viewsets.ModelViewSet):
    queryset = Policies.objects.all().order_by('name')
    serializer_class = PoliciesSerializer

class SeaRegionsViewSet(viewsets.ModelViewSet):
    queryset = SeaRegions.objects.all().order_by('name')
    serializer_class = SeaRegionsSerializer

class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all().order_by('name')
    serializer_class = StandardsSerializer

class ThemesViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all().order_by('name')
    serializer_class = ThemesSerializer

class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all().order_by('name')
    serializer_class = TypesSerializer
