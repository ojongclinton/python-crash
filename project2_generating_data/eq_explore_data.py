from pathlib import Path
import json

path = Path('weather_data/eq_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)


all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags,lons,lats = [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lats.append(lat) 
    lons.append(lon)

print(mags[:10])
print(lats[:10])
print(lons[:10])
