"""odiscat_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from api import views as api_views
from dashboard import views as dash_views

from django.conf.urls import url
#from restcrudswagger import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'catalogue', api_views.CatalogueViewSet)
router.register(r'catalogue_relations', api_views.CatalogueRelationsViewSet)
router.register(r'catalogue_relations_goos_eovs', api_views.CatalogueRelationsGoosEovsViewSet)
router.register(r'catalogue_contributed_to', api_views.CatalogueContributedtoViewSet)
router.register(r'catalogue_dois', api_views.CatalogueDoisViewSet)
router.register(r'catalogue_m2m_technologies', api_views.CatalogueM2MtechnologiesViewSet)
router.register(r'catalogue_obtained_from', api_views.CatalogueObtainedfromViewSet)
router.register(r'catalogue_sea_regions', api_views.CatalogueSeaRegionsViewSet)
router.register(r'catalogue_themes', api_views.CatalogueThemesViewSet)
router.register(r'catalogue_types', api_views.CatalogueTypesViewSet)
router.register(r'data_systems', api_views.DataSystemsViewSet)
router.register(r'dois', api_views.DoisViewSet)
router.register(r'keywords', api_views.KeywordsViewSet)
router.register(r'm2m_technologies', api_views.M2MtechnologiesViewSet)
router.register(r'policy', api_views.PoliciesViewSet)
router.register(r'sea_regions', api_views.SeaRegionsViewSet)
router.register(r'standards', api_views.StandardsViewSet)
router.register(r'themes', api_views.ThemesViewSet)
router.register(r'types', api_views.TypesViewSet)

schema_view = get_swagger_view(title='ODISCat-API')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dashboard/', dash_views.dashboard_index, name='index'),
    path('sendjson/', dash_views.send_json, name='send_json'),
    url(r'^$', schema_view),
    #path('swagger/', schema_view),
    #path('swagger/', include(router.urls))
    url(r'^', include(router.urls))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
