import pandas as pd
import geopy.distance

main_data = pd.read_csv("Main_DATA_FILE.csv")
main_data_clean = pd.DataFrame()

unique_chargers = main_data.drop_duplicates(subset=['Station Name'])
unique_chargers_distances = pd.DataFrame(columns=['Station Name', 'Within 10m', 'Within 100m', 'Within 1000m'])
unique_chargers_distances['Station Name'] = unique_chargers['Station Name']

#unique_chargers.to_csv("unique_chargers.csv")

print(unique_chargers_distances)

#print(geopy.distance.geodesic(((unique_chargers.iloc[84]['Latitude']), (unique_chargers.iloc[84]['Longitude'])), ((unique_chargers.iloc[87]['Latitude']), (unique_chargers.iloc[87]['Longitude']))).m)

def distance(row1, row2):
    return geopy.distance.geodesic(((unique_chargers.iloc[row1]['Latitude']), (unique_chargers.iloc[row1]['Longitude'])), ((unique_chargers.iloc[row2]['Latitude']), (unique_chargers.iloc[row2]['Longitude']))).m

for a in range(122):
    for b in range(122):
        ten_list = []
        hundred_list = []
        thousand_list = []
        if b != a:
            if distance(a, b) <= 10:
                ten_list.append(unique_chargers.iloc[b]['Station Name'])
            elif distance(a, b) <= 100:
                hundred_list.append(unique_chargers.iloc[b]['Station Name'])
            elif distance(a, b) <= 1000:
                thousand_list.append(unique_chargers.iloc[b]['Station Name'])
    ten_list = ', '.join(ten_list)
    hundred_list = ', '.join(hundred_list)
    thousand_list = ', '.join(thousand_list)
    unique_chargers_distances.at[a, 'Within 10m'] = ten_list
    unique_chargers_distances.at[a, 'Within 100m'] = hundred_list
    unique_chargers_distances.at[a, 'Within 1000m'] = thousand_list

print(unique_chargers_distances)
#unique_chargers_distances.to_csv("unique_chargers_distances.csv")



"""
IGNORE EVERYTHING DOWN HERE
"""





"""
unique_chargers['Port Number'] = unique_chargers['Port Number'].str[:1].astype(int)
multiple_port_chargers = unique_chargers[unique_chargers['Port Number'] > 1]
other_chargers = unique_chargers[unique_chargers['Port Number'] == 1]
print(multiple_port_chargers)
print(other_chargers)

multiple_port_chargers.to_csv("multiple_port_chargers.csv")
"""


"""
for a in range(122):
    for b in range(122):
        temp_list = ['placeholder']
        if geopy.distance.geodesic(((unique_chargers.iloc[a]['Latitude']), (unique_chargers.iloc[a]['Longitude'])), ((unique_chargers.iloc[b]['Latitude']), (unique_chargers.iloc[b]['Longitude']))).m <= 100:
            temp_list.append(unique_chargers.iloc[a]['Station Name'])
            print(temp_list)
    unique_chargers_distances.loc[a, 'Close Chargers'] = ', '.join(temp_list)
    print(', '.join(temp_list))
"""

#unique_chargers_distances.to_csv("unique_chargers_distances.csv")