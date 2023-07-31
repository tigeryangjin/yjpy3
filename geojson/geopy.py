import json
import geo_converters as convert

geojson_str = []
with open('yj.geojson', 'r', encoding='UTF-8') as f1:
    geojson_str.append(f1.read())

# print(geojson_str[0])

area_dict = {}
area_json = json.loads(geojson_str[0])['features']
print(type(area_json))
for features in area_json:
    area_code = features['properties']['id']
    if area_code not in area_dict.keys():
        area_dict[area_code] = {}
        area_dict[area_code]['area_info'] = '%s' % features['properties']['name']
        area_dict[area_code]['geometry'] = features['geometry']
# print(geojson_str)
print(type(area_dict))
print(area_dict[1])
print(area_dict[2])
