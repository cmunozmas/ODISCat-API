from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import json
import requests
import os
import re
import random
import colour
import randomcolor
import numpy as np
from django.http import JsonResponse
from api.models import Catalogue, CatalogueTypes, CatalogueThemes, Themes, Types, Standards, M2Mtechnologies, Keywords
from django.db.models import Count

def dashboard_index(request):
    # Total numbers
    template = loader.get_template('custom/index.html')
    total_records = str(Catalogue.objects.all().count())
    total_themes = str(Themes.objects.all().count())
    total_types = str(Types.objects.all().count())
    total_standards = str(Standards.objects.all().count())
    total_m2m = str(M2Mtechnologies.objects.all().count())
    total_keywords = str(Keywords.objects.all().count())

    # records creation
    records_timeline = Catalogue.objects.values('entry_date').annotate(total=Count('entry_date')).order_by('entry_date')
    for i in range(0,len(records_timeline)):
        if i == 0:
            records_timeline[i]['total_cumsum'] = records_timeline[i]['total']
        elif i > 0:
            records_timeline[i]['total_cumsum'] = records_timeline[i-1]['total_cumsum'] + records_timeline[i]['total']
    print(records_timeline)

    # Policies
    policies_unknown = str(Catalogue.objects.filter(md_policy=0).all().count())
    policies_open = str(Catalogue.objects.filter(md_policy=1).all().count())
    policies_open_registration = str(Catalogue.objects.filter(md_policy=2).all().count())
    policies_restricted = str(Catalogue.objects.filter(md_policy=3).all().count())
    policies_metadata = str(Catalogue.objects.filter(md_policy=4).all().count())
    sorted_countries = get_countries(request)

    # Catalogue types
    types = Types.objects.all().values('name')
    catalogue_types = CatalogueTypes.objects.all().values('types').annotate(type_count=Count('types'))
    for i in range(0, len(catalogue_types)):
        catalogue_types[i]['name'] = types[i]['name']
    all_catalogue_types = {
    k: [d.get(k) for d in catalogue_types]
    for k in set().union(*catalogue_types)
    }
    types = sum(all_catalogue_types['type_count'])
    for i in range(0, len(catalogue_types)):
        catalogue_types[i]['percent'] = (catalogue_types[i]['type_count']*100)/(int(types))

    # Catalogue Themes
    themes = Themes.objects.all().values('name')
    catalogue_themes = CatalogueThemes.objects.all().values('themes').annotate(theme_count=Count('themes'))
    colors = randomcolor.RandomColor().generate(hue="blue", count=18)
    for i in range(0, len(catalogue_themes)):
        catalogue_themes[i]['name'] = themes[i]['name']
        catalogue_themes[i]['color'] = colors[i]
    all_catalogue_themes = {
    k: [d.get(k) for d in catalogue_themes]
    for k in set().union(*catalogue_themes)
    }

    context = {'total_records': total_records, 'total_themes': total_themes, 'total_types': total_types,
                'total_standards': total_standards, 'total_m2m': total_m2m, 'total_keywords': total_keywords,
                'records_timeline': records_timeline,
                'policies_open': policies_open, 'policies_open_registration':policies_open_registration,
                'policies_restricted':policies_restricted, 'policies_metadata': policies_metadata, 'policies_unknown': policies_unknown,
                'country_name_0': str(sorted_countries[0][0]), 'country_value_0': str(sorted_countries[0][1]),
                'country_name_1': str(sorted_countries[1][0]), 'country_value_1': str(sorted_countries[1][1]),
                'country_name_2': str(sorted_countries[2][0]), 'country_value_2': str(sorted_countries[2][1]),
                'country_name_3': str(sorted_countries[3][0]), 'country_value_3': str(sorted_countries[3][1]),
                'country_name_4': str(sorted_countries[4][0]), 'country_value_4': str(sorted_countries[4][1]),
                'catalogue_types': catalogue_types, 'catalogue_themes': catalogue_themes,
                }
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html')

def get_countries(request):
    query = Catalogue.objects.all().values('ds_site_countries').annotate(country_count=Count('ds_site_countries'))
    countries = {}
    for i in range(0, len(query)):
        if ';' in query[i]['ds_site_countries']:
            countries_list = re.split(';', query[i]['ds_site_countries'])
            for country_name in countries_list:
                if country_name in countries:
                    countries.update( { country_name: str(int(countries[country_name]) + 1) } )
                else:
                    countries.update( { country_name: '1' } )
        else:
            countries.update( { query[i]['ds_site_countries']:query[i]['country_count'] } )
    del countries['GLOBAL']
    del countries['REGIONAL']
    dirname = os.path.dirname(__file__)
    filehandler = open(dirname + '/static/vendors/jqvmap/examples/js/jquery.vmap.odiscat_owning_countries.js', 'wt')
    data = 'var sample_data = ' + str(countries).lower() + ';'
    filehandler.write(data)
    filehandler.close()
    for keys in countries:
        countries[keys] = int(countries[keys])
    sorted_countries = sorted(countries.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_countries

# def index(request):
#     records_response = requests.get('http://127.0.0.1:8000/catalogue/?format=json').text
#     #records_response_info = json.loads(records_response)
#     records_df = pd.read_json(records_response)
#     total_records = len(records_response_info)
#     policies  = records_df.groupby('md_policy').count()
#     policies_open_count = policies.id[0]
#     policies_openreg_count = policies.id[1]
#     policies_meta_count = policies.id[2]
#     policies_restrict_count = policies.id[3]
#     policies_unknown_count = policies.id[4]
#
#     context = {'total_records': total_records}
#     # context = {'total_records': total_records,
#     # 'policies_open_count': policies_open_count,
#     # 'policies_openreg_count': policies_openreg_count,
#     # 'policies_meta_count': policies_openreg_count,
#     # 'policies_restrict_count': policies_restrict_count,
#     # 'policies_unknown_count': policies_openreg_count
#     # }
#     template = loader.get_template('custom/index.html')
#     return HttpResponse(template.render(context, request))

# def obps_history(request):
#     users_total_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('users_num_total')).get('sum')
#     users_new_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('users_num_new')).get('sum')
#     #docs_access_num_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('docs_access_num')).get('sum')
#     docs_access_num_sum = Ganalytics_obpsorg_docs.objects.aggregate(sum=Sum('sessions')).get('sum')
#     visits_num_sum = Ganalytics_obpsorg.objects.aggregate(sum=Sum('visits_num')).get('sum')
#     dates_list = Ganalytics_obpsorg.objects.values('date_start')
#     users_new_list = Ganalytics_obpsorg.objects.values('users_num_new')
#     ganalytics_obpsorg_data = Ganalytics_obpsorg.objects.order_by('date_start')
#
#     count_countries = str(Ganalytics_obpsorg_countries.objects.all().count())
#
#     countries_df = pd.DataFrame(list(Ganalytics_obpsorg_countries.objects.all().values('country', 'users', 'sessions')))
#     countries_df = countries_df.sort_values(by='users', ascending=False).head(20)
#
#     pagepaths_df = pd.DataFrame(list(Ganalytics_obpsorg_docs.objects.all().values('doc_path', 'users', 'sessions')))
#     pagepaths_df = pagepaths_df.sort_values(by='users', ascending=False).head(20)
#
#     # convert doc_path into URLs to ba accessed from frontend
#     for i in range(0,len(pagepaths_df)):
#         doc_path = pagepaths_df['doc_path'].iloc[i]
#         doc_path = doc_path.rsplit('/',1)[0]
#         pagepaths_df['doc_path'].iloc[i] = doc_path
#     pagepaths_df['doc_path'] = pagepaths_df['doc_path'].str.replace(r'/bitstream', 'https://www.oceanbestpractices.net')
#
#     context= {'total_users_sum': users_total_sum, 'total_new_users_sum': users_new_sum,
#             'total_docs_access_sum': docs_access_num_sum, 'visits_num_sum': visits_num_sum,
#             'dates': dates_list, 'new_users': users_new_list, 'ganalytics_obpsorg_data': ganalytics_obpsorg_data,
#             'countries_count': count_countries, 'countries_df': countries_df, 'pagepaths_df': pagepaths_df}
#
#     return render(request, 'obps_history.html', context)





# def test(request):
#     """ view function for sales app """
#
#     # read data
#
#     df = pd.read_csv("/home/a33272/Desktop/car_sales.csv")
#     rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
#     categories = list(rs.index)
#     values = list(rs.values)
#
#     table_content = df.to_html(index=None)
#     table_content = table_content.replace("","")
#     table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
#     table_content = table_content.replace('border="1"',"")
#
#     context = {"categories": categories, 'values': values, 'table_data':table_content}
#     return render(request, 'test.html', context=context)

from django.http import JsonResponse
def send_json(request):

    data = { "nodes": [
            { "id": 1, "name": "SOCIB DC" },
            { "id": 2, "name": "SOCIB THREDDS Server" },
            { "id": 3, "name": "SOCIB Real-Time Monitor" },
            { "id": 4, "name": "SOCIB CTD Profiles Viewer" },
            { "id": 5, "name": "SOCIB Modelling Facility" },
            { "id": 6, "name": "SOCIB HF-Radar Facility" },
            { "id": 7, "name": "IBISAR" }
          ],
          "links": [
            { "source": 1, "target": 2 },
            { "source": 1, "target": 3 },
            { "source": 1, "target": 4 },
            { "source": 1, "target": 5 },
            { "source": 1, "target": 6 },
            { "source": 1, "target": 7 }
          ]}

    return JsonResponse(data, safe=False)
