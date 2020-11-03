import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data

filename = 'eq_data_30_day_m1.json'
with open(filename) as f: 
    eq_data = json.load(f)

readable_file = 'readable_eq_data_my_copy.json'
with open(readable_file, 'w') as f: 
    json.dump(eq_data, f, indent=4) 

all_eq_dict = eq_data['features'] 


mags, lons, lats, hover_text = [], [], [], [] 
for eq_dict in all_eq_dict: 
    mag = eq_dict['properties']['mag'] 
    lon = eq_dict['geometry']['coordinates'][0]
    lat= eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title'] 
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)



data = [{
    'type': 'scattergeo', 
    'lon' : lons, 
    'lat' : lats,
    'text' : hover_text, 
    'marker': {
        'size': [3*mag for mag in mags], 
        'color': mags, 
        'colorscale': 'Viridis', 
        'reversescale': True, 
        'colorbar': {'title': 'magnitude'}, 
    }, 
}]
my_layout = Layout(title = 'Global Earthquakes') 

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')