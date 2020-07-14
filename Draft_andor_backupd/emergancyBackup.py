### Imports
import io
import re
import json
import requests
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
import matplotlib.colors as colors
from pandas.io.json import json_normalize

# graphing 
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
%matplotlib inline

### Install Imports then Import them!
# import folium if cant install then import
try:
    import folium
except:
    !pip install folium
    print("installed {}".format('folium'))
    import folium
    
# import wikipedia if cant install then import
try:
    import wikipedia as wp
except:
    !pip install wikipedia
    print("installed {}".format('wikipedia'))
    import wikipedia

# zip code stuff
try:
    import uszipcode
except:
    !pip install uszipcode
    print("installed {}".format('uszipcode'))
    import uszipcode
    
from uszipcode import Zipcode
from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=True)

# graph imports 
try:
    import geopy 
    from geopy.geocoders import Nominatim
except:
    !pip install geopy
    print("installed {}".format('geopy'))
    import geopy 
    from geopy.geocoders import Nominatim

# learn imports
try:
    import seaborn as sns
except:
    !pip install seaborn
    print("installed {}".format('seaborn'))
    import seaborn as sns
    
from sklearn.cluster import KMeans



### Declare City List
city_list = [
    'Baltimore',
    'Baltimore County',
    'Richmond',
    'Henrico County',
    'Phoenix',
    'Maricopa County',
    'Houston',
    'Harris County'
]

### Declare City List with State

city_state = [
    ['Baltimore', 'Maryland'],
    ['Baltimore County', 'Maryland'],
    ['Richmond', 'Virginia'],
    ['Henrico County', 'Virginia'],
    ['Phoenix', 'Arizona'],
    ['Maricopa County', 'Arizona'],
    ['Houston', 'Texas'],
    ['Harris County', 'Texas']
]

### Declare Codinates DataFram

header = ['City', 'Latitude', 'Longitude']
comb = [
    ['Baltimore', 39.283333, -76.616667],
    ['Baltimore County', 39.4, -76.6],
    ['Richmond', 37.533333, -77.466667],
    ['Henrico County', 37.55, -77.4],
    ['Phoenix', 33.45, -112.066667],
    ['Maricopa County', 33.513889, -112.475833],
    ['Houston', 29.762778, -95.383056],
    ['Harris County', 29.86, -95.39]
]

tempC = []
tempLat = []
tempLong = []
for c in comb:
    tempC.append(c[0])
    tempLat.append(c[1])
    tempLong.append(c[2])

#NDF = new dataframe
NDF = {
    str(header[0]): tempC,
    str(header[1]): tempLat,
    str(header[2]): tempLong
}

# CDF = cords dataframe
CDF = pd.DataFrame(NDF, columns = ['City', 'Latitude', 'Longitude'])

cities = CDF[header[0]]
lat = CDF[header[1]]
long = CDF[header[2]]

### Foursquare Creds

CLIENT_ID = 'TL2E0LDIYOXQH22H13SIGIGDAZRVEF4HCZSM0KQ2XJKXDHKK' # foursquare ID
CLIENT_SECRET = 'U0YKWNDNGW22DNPJMM4CXUKRDMJH2CII0PPRFISGL3HZLUHP' # foursquare Secret
VERSION = '20200712'
LIMIT = 100

### Initialize Maps V1

# lets start with the 4 main cities
#print(cities)
#print(lat)
#print(long)

baltimore_city_map = folium.Map(location=[lat[0], long[0]], zoom_start=10)
baltimore_county_map = folium.Map(location=[lat[1], long[1]], zoom_start=10)
richmond_city_map = folium.Map(location=[lat[2], long[2]], zoom_start=10)
henrico_county_map = folium.Map(location=[lat[3], long[3]], zoom_start=10)
phoenix_city_map = folium.Map(location=[lat[4], long[4]], zoom_start=10)
maricopa_county_map = folium.Map(location=[lat[5], long[5]], zoom_start=10)
houston_city_map = folium.Map(location=[lat[6], long[6]], zoom_start=10)
harris_county_map = folium.Map(location=[lat[7], long[7]], zoom_start=10)

# lc = location class
# add them all to a list
maps = [
    baltimore_city_map, # lc1
    baltimore_county_map, # lc1
    richmond_city_map, # lc2
    henrico_county_map, # lc2
    phoenix_city_map, # lc3
    maricopa_county_map, # lc3
    houston_city_map, # lc4
    harris_county_map # lc4
]

### Get all Zips

all_zip = []

# search for all the zips and add them to a list
for cs in city_state:
    temp1 = search.by_city_and_state(cs[0], cs[1])
    for t in temp1:
        tempL = [cs[0]]
        tempL.append(t.zipcode)
        if len(t.common_city_list) != 0:
            tempL.append(t.common_city_list[-1])
        else:
            tempL.append(cs[0]+'?')
        tempL.append(t.lat)
        tempL.append(t.lng)
        all_zip.append(tempL)

# format for all_zip [[city, zip, common city, lat, long]]

# remove the none from the cord and put the previous val in
prevE = []
for az in all_zip:
    if az[3] == None:
        az[3] = prevE[-1][0]
    if az[4] == None:
        az[4] = prevE[-1][-1]
    
    temp = [az[3], az[4]]
    prevE.append(temp)
    
### Turn all_zips into a DataFrame

header = ['City', 'Zip', 'Common City', 'Latitude', 'Longitude']
TC = []
TZ = []
TCC = []
TLo = []
TLa = []

for az2 in all_zip:
    TC.append(az2[0])
    TZ.append(az2[1])
    TCC.append(az2[2])
    TLo.append(az2[3])
    TLa.append(az2[4])

tNDF = {
    header[0]:TC,
    header[1]:TZ,
    header[2]:TCC,
    header[3]:TLo,
    header[4]:TLa
}

all_zipDF = pd.DataFrame(tNDF, columns = ['City', 'Zip', 'Common City', 'Latitude', 'Longitude'])

all_zipDF.head()

### Make Labels

labels = []
for c in cities:
    temp = folium.Popup(c)
    labels.append(temp)

### Make Circle Markers

# cm = Circle Markers
cm = []

x = 0

while x != 8:
    folium.CircleMarker(
        [lat[x], long[x]],
        radius=5,
        popup=labels[x],
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(maps[x])
    x += 1

### Initialize Maps V2

# all_zipDF
# centers with baltimore
addr = 'Baltimore'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(addr)
latitude = location.latitude
longitude = location.longitude
#print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))

main_map2 = folium.Map(location=[latitude, longitude], zoom_start=10)

for lat, lng, city, CC in zip(all_zipDF['Latitude'], all_zipDF['Longitude'], all_zipDF['City'], all_zipDF['Common City']):
    label = '{}, {}'.format(city, CC)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(main_map2)

    
main_map2

### Get Venues

# FourSqure url
url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, 500, LIMIT)

results = requests.get(url).json()
results

# assign relevant part of JSON to venues
venues = results['response']['venues']

# tranform venues into a dataframe
dataframe = json_normalize(venues)

#dataframe.head()

# keep only columns that include venue name, and anything that is associated with location
fc = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']
dataframe_filtered = dataframe.loc[:, fc]

# filter the category for each row
dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)

# clean column names by keeping only last term
dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]

dataframe_filtered.head()

### Function to get venues

def getNearbyVenues(names, latitudes, longitudes, radius=500):
    
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        #print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
            
        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        # return only relevant information for each nearby venue
        venues_list.append([(
            name, 
            lat, 
            lng, 
            v['venue']['name'], 
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['City', 
                  'City Latitude', 
                  'City Longitude', 
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
        
    return(nearby_venues)

### List all nearby venues

all_venues = getNearbyVenues(names=all_zipDF['City'],
                                   latitudes=all_zipDF['Latitude'],
                                   longitudes=all_zipDF['Longitude']
                                  )


### Venues

print('{} Venues were returned by Foursquare.'.format(all_venues.shape[0]))

### Number of venues per Neighborhood

all_venues.groupby('City').count()

# unique categories
print('There are {} uniques categories.\n\n'.format(len(all_venues['Venue Category'].unique())))

# one hot encoding
all_onehot = pd.get_dummies(all_venues[['Venue Category']], prefix="", prefix_sep="")

# add neighborhood column back to dataframe
all_onehot['City'] = all_venues['City'] 

# move neighborhood column to the first column
fixed_columns = [all_onehot.columns[-1]] + list(all_onehot.columns[:-1])
manhattan_onehot = all_onehot[fixed_columns]

all_onehot.head()

all_grouped = all_onehot.groupby('City').mean().reset_index()
all_grouped.head()

### Return common venues

def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]

### Top Venues

num_top_venues = 5

indicators = ['st', 'nd', 'rd']

# create the columns according to number of top venues
columns = ['City']

for ind in np.arange(num_top_venues):
    try: 
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))
        
# create a new dataframe
neighborhoods_venues_sorted = pd.DataFrame(columns=columns)

neighborhoods_venues_sorted['City'] = all_grouped['City']

for ind in np.arange(all_grouped.shape[0]):
    neighborhoods_venues_sorted.iloc[ind, 1:] = return_most_common_venues(all_grouped.iloc[ind, :], num_top_venues)


    
neighborhoods_venues_sorted.head()

### Get Population & Population Density

Pheader = ['City', 'Zip', 'Population', 'Population Density']
Pcity = all_zipDF['City']
Pzip = all_zipDF['Zip']
popL = []
popDL = []

for z in Pzip:
    temp = search.by_zipcode(z)
    pop = temp.population
    popD = temp.population_density
    
    #print("{} || pop: {} || pop dense {}\n".format(z, temp.population, temp.population_density))

    if pop != None or popD != None:
        popL.append(pop)
        popDL.append(popD)
    else:
        popL.append(np.nan)
        popDL.append(np.nan)
        
popNDF = {
    Pheader[0]: Pcity,
    Pheader[1]: Pzip,
    Pheader[2]: popL,
    Pheader[3]: popDL
}

popDF = pd.DataFrame(popNDF, columns = ['City', 'Zip', 'Population', 'Population Density'])
popDF = popDF.dropna()
popDF

### Get Minium Function

def getMin(l1): # l1 is a list
    #print(min(l1))
    return min(l1)

### Get Maxium Function

def getMax(l1): # l1 is a list
    #print(max(l1))
    return max(l1)

### Plot testing

p = popDF
TP = p['Population']
TPD = p['Population Density']

TP_min = getMin(TP)
TP_max = getMax(TP)
TPD_min = getMin(TPD)
TPD_max = getMax(TPD)
bg = [TP_min/10, TP_max/100, TPD_min*10, TPD_max/10] # bar graph data
x = ['Pop Min', 'Pop Max/100', 'Pop Den Min*100', 'Pop Den Max']

plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(bg)]

plt.bar(x_pos, bg, color='green')

plt.xticks(x_pos, x)
plt.xlabel('Population Data')
plt.ylabel('Value')
plt.title('Population Graph')
plt.show()

### Get all Venue Categories

Category
mlv = [] # master venue list
​
x = 0
for y in all_venues['Venue Category']:
    if y not in mlv:
        mlv.append(y)
    x += 1

mlv

### Get all Restaurants Categories

h1 = list(all_grouped.columns)

RC = [] # RC means Restaurants Categories
# ask the user to verify if its a restaurant
for h in h1:
    print("Is {} a Restaurant?".format(h))
    check1 = input('y for yes or n for no:\t')
    
    if check1 == 'y':
        RC.append(h)
        
len(RC)

### Get all Venue names with the correct Category

# get from dataframe_filtered['name']
#dataframe_filtered.tail()

h3 = list(all_venues.columns)
restaurants1 = []

for index, row in all_venues.iterrows():
    if row[6] in RC:
        restaurants1.append(list(row))

#restaurants1
rd = pd.DataFrame(restaurants1, columns = h3)
rd.head()

### Map all good Restaurants

addr3 = "Baltimore"

RV =getNearbyVenues(names=rd['City'],
                                   latitudes=rd['Venue Latitude'],
                                   longitudes=rd['Venue Longitude']
                                  )

print('{} are returned Venues.'.format(RV.shape[0]))