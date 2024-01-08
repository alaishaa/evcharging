import pandas as pd
import geopy.distance

unique_chargers = pd.read_csv("unique_chargers.csv")
poi_points = pd.read_csv("poi_point.csv")
traffic = pd.read_csv("lat_long_traffic_clean.csv")

output_csv = pd.DataFrame(columns=['Station Name', 'poi number 10m', 'poi number 100m', 'poi number 1000m', 'traffic avg 1000m'])
output_csv['Station Name'] = unique_chargers['Station Name']

for a in range(122):
    poi1000 = 0
    poi100 = 0
    poi10 = 0
    for b in range(len(poi_points)):
        if geopy.distance.geodesic(((unique_chargers.iloc[a]['Latitude']), (unique_chargers.iloc[a]['Longitude'])), ((poi_points.iloc[b]['Y']), (poi_points.iloc[b]['X']))).m <= 1000:
            poi1000 += 1
        if geopy.distance.geodesic(((unique_chargers.iloc[a]['Latitude']), (unique_chargers.iloc[a]['Longitude'])), ((poi_points.iloc[b]['Y']), (poi_points.iloc[b]['X']))).m <= 100:
            poi100 += 1
        if geopy.distance.geodesic(((unique_chargers.iloc[a]['Latitude']), (unique_chargers.iloc[a]['Longitude'])), ((poi_points.iloc[b]['Y']), (poi_points.iloc[b]['X']))).m <= 10:
            poi10 += 1

    output_csv.at[a, 'poi number 10m'] = poi10
    output_csv.at[a, 'poi number 100m'] = poi100
    output_csv.at[a, 'poi number 1000m'] = poi1000

    traffic_list = []
    average_traffic = 0
    for c in range(len(traffic)):
        if geopy.distance.geodesic(((unique_chargers.iloc[a]['Latitude']), (unique_chargers.iloc[a]['Longitude'])), ((traffic.iloc[c]['LATITUDE']), (traffic.iloc[c]['LONGITUDE']))).m <=1000:
            traffic_list.append(traffic.iloc[c]['START_ACCUM'])
    for n in traffic_list:
        average_traffic += n
    if len(traffic_list) != 0:
        average_traffic /= len(traffic_list)

    output_csv.at[a, 'traffic avg 1000m'] = average_traffic

output_csv.to_csv('poi_nums_and_traffic_avg.csv')