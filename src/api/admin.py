from django.contrib import admin
from .models import Catalogue, CatalogueContributedto, CatalogueDois, CatalogueM2Mtechnologies, CatalogueObtainedfrom, CatalogueThemes, CatalogueTypes,DataSystems, Dois, Keywords, M2Mtechnologies, Policies, SeaRegions, Standards, Themes, Types



# Register your models here.

class CatalogueAdmin(admin.ModelAdmin):
    #list_display = ('ds_name_english', 'md_policy', 'md_standard',)
    list_display = ('ds_name_english', 'md_policy', )
class DataSystemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class DoisAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class M2MtechnologiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class PoliciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class SeaRegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class StandardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(CatalogueContributedto)
admin.site.register(CatalogueDois)
admin.site.register(CatalogueM2Mtechnologies)
admin.site.register(CatalogueObtainedfrom)
admin.site.register(CatalogueThemes)
admin.site.register(CatalogueTypes)
admin.site.register(DataSystems, DataSystemsAdmin)
admin.site.register(Dois, DoisAdmin)
admin.site.register(Keywords, KeywordsAdmin)
admin.site.register(M2Mtechnologies, M2MtechnologiesAdmin)
admin.site.register(Policies, PoliciesAdmin)
admin.site.register(SeaRegions, SeaRegionsAdmin)
admin.site.register(Standards, StandardsAdmin)
admin.site.register(Themes, ThemesAdmin)
admin.site.register(Types, TypesAdmin)
