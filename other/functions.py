# functions.py
# system imports
import re
import config
import requests
import string
# data imports
import pandas as pd
import wikipedia as wp # this pulls from wikipedia

# time functions
import time
import datetime
from datetime import date
from time import sleep as s
from datetime import datetime

# file i/o
import csv

def writeBaltimorePopulation():
    """
    Table info:
    Title: Historical population
    Original headers: [ Census, Pop., Unnamed: 2_level_1, %Â± ]
    New headers: ["Census", "Pop.", "Percent"]
    """
    
    file1 = config.data_path + "balt_pop.csv"
    NH = ["Census", "Population", "Percent"] # new header
    html = wp.page("Baltimore: Population").html().encode('UTF-8')
    df = pd.read_html(html)[4] # data location of the table
    #print(df.head())
    cen = df['Historical population']['Census'] # census year
    pop = df['Historical population']['Pop.'] # population
    perc = df['Historical population']['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        'Population': pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", "Population", "Percent"])

    # delete the first and last row
    dataOut = dataOut.drop([24])
    dataOut = dataOut.drop([0])

    for index, row in dataOut.iterrows():
        if 'â' in str(row['Percent']):
            row['Population'].strip('â')
        if 'Est. ' in str(row['Census']):
            row['Census'].strip('Est. ')

    dataOut.to_csv(file1, encoding='UTF-8', index=False)


def writeHoustonPopulation():
    """
    Table info:
    Title: Historical population
    Original headers: [ Census, Pop., Unnamed: 2_level_1, %Â± ]
    New headers: ["Census", "Pop.", "Percent"]
    """
    
    file1 = config.data_path + "hou_pop.csv"
    NH = ["Census", "Population", "Percent"] # new header
    html = wp.page("Houston: Population").html().encode('UTF-8')
    df = pd.read_html(html)[3] # data location of the table
    #print(df.head())
    cen = df['Historical population']['Census'] # census year
    pop = df['Historical population']['Pop.'] # population
    perc = df['Historical population']['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        'Population': pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", "Population", "Percent"])

    # delete the first and last row
    dataOut = dataOut.drop([18])
    dataOut = dataOut.drop([0])

    for index, row in dataOut.iterrows():
        if 'â' in str(row['Percent']):
            row['Population'].strip('â')
        if 'Est. ' in str(row['Census']):
            row['Census'].strip('Est. ')

    dataOut.to_csv(file1, encoding='UTF-8', index=False)

def writeRichmondPopulation():
    """
    Table info:
    Title: Historical population
    Original headers: [ Census, Pop., Unnamed: 2_level_1, %Â± ]
    New headers: ["Census", "Pop.", "Percent"]
    """
    
    file1 = config.data_path + "rich_pop.csv"
    NH = ["Census", "Population", "Percent"] # new header
    html = wp.page("Richmond, Virginia: Population").html().encode('UTF-8')
    df = pd.read_html(html)[2] # data location of the table
    #print(df.head())
    cen = df['Historical population']['Census'] # census year
    pop = df['Historical population']['Pop.'] # population
    perc = df['Historical population']['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        'Population': pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", "Population", "Percent"])

    # delete the first and last row
    dataOut = dataOut.drop([24])
    dataOut = dataOut.drop([0])

    for index, row in dataOut.iterrows():
        if 'â' in str(row['Percent']):
            row['Population'].strip('â')
        if 'Est. ' in str(row['Census']):
            row['Census'].strip('Est. ')

    dataOut.to_csv(file1, encoding='UTF-8', index=False)

def writePhoenixPopulation():
    """
    Table info:
    Title: Historical population
    Original headers: [ Census, Pop., Unnamed: 2_level_1, %Â± ]
    New headers: ["Census", "Pop.", "Percent"]
    """
    
    file1 = config.data_path + "phx_pop.csv"
    NH = ["Census", "Population", "Percent"] # new header
    html = wp.page("Phoenix, Arizona: Population").html().encode('UTF-8')
    df = pd.read_html(html)[6] # data location of the table
    #print(df.head())
    cen = df['Historical population']['Census'] # census year
    pop = df['Historical population']['Pop.'] # population
    perc = df['Historical population']['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        'Population': pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", "Population", "Percent"])

    # delete the first and last row
    dataOut = dataOut.drop([16])
    dataOut = dataOut.drop([0])

    for index, row in dataOut.iterrows():
        if 'â' in str(row['Percent']):
            row['Population'].strip('â')
        if 'Est. ' in str(row['Census']):
            row['Census'].strip('Est. ')

    dataOut.to_csv(file1, encoding='UTF-8', index=False)


def writeCords():
    
    file1 = config.data_path + 'lat_long.csv'
    header = ['City', 'Latitude', 'Longitude']
    baltimore = ['Baltimore', 39.283333, -76.616667]
    baltimoreCounty = ['Baltimore County', 39.4, -76.6]
    richmondCity = ['Richmond', 37.533333, -77.466667] # located in Henrico County
    henricoCounty = ['Henrico County', 37.55, -77.4]
    phoenix = ['Phoenix', 33.45, -112.066667] # located in Maricopa County
    maricopaCounty = ['Maricopa County', 33.513889, -112.475833]
    houston = ['Houston', 29.762778, -95.383056] # located in Harris County
    harrisCounty = ['Harris County', 29.86, -95.39]

    # all of above combined
    comb = [
        ['City', 'Latitude', 'Longitude'],
        ['Baltimore', 39.283333, -76.616667],
        ['Baltimore County', 39.4, -76.6],
        ['Richmond', 37.533333, -77.466667],
        ['Henrico County', 37.55, -77.4],
        ['Phoenix', 33.45, -112.066667],
        ['Maricopa County', 33.513889, -112.475833],
        ['Houston', 29.762778, -95.383056],
        ['Harris County', 29.86, -95.39]
    ]

    with open(file1, "w", newline="") as f1:
        cw = csv.writer(f1)
        for c in comb:
            cw.writerow(c)
    f1.close()

def retDict():
    city_list_other = {
        'Baltimore':{
            'Counties':['Prince Georges', 'Calvert'],
            'Counties_cords':[[38.83, -76.85], [38.53, -76.53]],
            'Counties_wiki_page':["Prince George's County, Maryland", 'Calvert County, Maryland'],
            'Counties_pop_table_num':[4, 3],
            'Cities':['Columbia', 'Germantown'],
            'Cities_cords':[[39.203611, -76.856944], [39.183333, -77.266667]],
            'Cities_wiki_page':['Columbia, Maryland', 'Germantown, Maryland'],
            'Cities_pop_table_num':[2, 2],
            'State': 'Maryland'
        },
        "Richmond":{
            'Counties':['Fairfax', 'Alexandria'],
            'Counties_cords':[[38.83, -77.28], [38.804722, -77.047222]],
            'Counties_wiki_page':['Fairfax County, Virginia', 'Alexandria, Virginia'],
            'Counties_pop_table_num':[6, 1],
            'Cities':['Virginia Beach', 'Norfolk'],
            'Cities_cords':[[36.85, -75.977778], [36.916667, -76.2]],
            'Cities_wiki_page':['Virginia Beach, Virginia', 'Norfolk, Virginia'],
            'Cities_pop_table_num':[3, 2],
            'State': 'Virginia'
        },
        "Phoenix":{
            'Counties':['La Paz', 'Yuma'],
            'Counties_cords':[[33.840278, -113.942778], [32.786944, -113.982778]],
            'Counties_wiki_page':['La Paz County, Arizona', 'Yuma County, Arizona'],
            'Counties_pop_table_num':[1, 3],
            'Cities':['Tucson', 'Mesa'],
            'Cities_cords':[[32.221667, -110.926389], [33.422222, -111.822778]],
            'Cities_wiki_page':['Tucson, Arizona', 'Mesa, Arizona'],
            'Cities_pop_table_num':[2, 4],
            'State': 'Arizona'
        },
        "Houston":{
            'Counties':['Brazoria', 'Montgomery'],
            'Counties_cords':[[29.17, -95.44], [30.3, -95.5]],
            'Counties_wiki_page':['Brazoria County, Texas', 'Montgomery County, Texas'],
            'Counties_pop_table_num':[1, 1],
            'Cities':['Dallas', 'Arlington'],
            'Cities_cords':[[32.779167, -96.808889], [32.705, -97.122778]],
            'Cities_wiki_page':['Dallas', 'Arlington, Texas'],
            'Cities_pop_table_num':[5, 2],
            'State': 'Texas'
        }
    }

    return city_list_other

def getPop(wikiName, dataL):
    s = "1234567890.%" # this gets rid of weird chars
    s2 = '1234567890'
    html = wp.page(wikiName).html().encode('UTF-8')
    print('Got the {} page'.format(wikiName))
    
    df = pd.read_html(html)[dataL]
    print(df.keys())
    k = df.keys()
    try:
        cen = df[str(k[1][0])]['Census'] # census year
        pop = df['Historical population']['Pop.'] # population
        perc = df['Historical population']['%Â±'] # percent change
    except:
        cen = df[str(k[1][0])]['Census'] # census year
        pop = df[str(k[1][0])]['Pop.'] # population
        perc = df[str(k[1][0])]['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        '{}-pop'.format(wikiName): pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", '{}-pop'.format(wikiName), "Percent"])
    
    # delete the first and last row
    dataOut = dataOut.drop([len(dataOut)-1])
    dataOut = dataOut.drop([0])

    printable = set(string.printable)
    
    for index, row in dataOut.iterrows():
        row['Percent'] = ''.join(filter(lambda x: x in printable, row['Percent']))
        if type(row['Census']) != int:
            row['Census'] = row['Census'].strip('Est. ')
    
    return dataOut

def r1():
    city_list_other = retDict()
    ALL_DFs = [] # all dataframe will be added to this list.
    t1 = city_list_other['Richmond']['Counties_wiki_page']
    t2 = city_list_other['Richmond']['Counties_pop_table_num']
    t3 = city_list_other['Richmond']['Cities_wiki_page']
    t4 = city_list_other['Richmond']['Cities_pop_table_num']

    ml =[
        [t1[0], t2[0]],
        [t1[1], t2[1]],
        [t3[0], t4[0]],
        [t3[1], t4[1]],
    ]

    for m in ml:
        tDF = getPop(m[0],m[1])
        ALL_DFs.append(tDF)


def writeRichmondPopulation2():
    """
    Table info:
    Title: Historical population
    Original headers: [ Census, Pop., Unnamed: 2_level_1, %Â± ]
    New headers: ["Census", "Pop.", "Percent"]
    """
    s = "1234567890.%" # this gets rid of weird chars
    s2 = '1234567890'
    
    file1 = config.data_path + "norfolk_pop.csv"
    NH = ["Census", "Population", "Percent"] # new header
    html = wp.page("Norfolk, Virginia").html().encode('UTF-8')
    df = pd.read_html(html)[2] # data location of the table
    #print(df.head())
    cen = df['Historical population']['Census'] # census year
    pop = df['Historical population']['Pop.'] # population
    perc = df['Historical population']['%Â±'] # percent change

    # NDF = new dataframe
    NDF = {
        'Census': cen,
        'Population': pop,
        'Percent': perc 
    }

    # convert to a better dataframe
    dataOut = pd.DataFrame(NDF, columns = ["Census", "Population", "Percent"])

    # delete the first and last row
    dataOut = dataOut.drop([24])
    dataOut = dataOut.drop([0])

    printable = set(string.printable)

    for index, row in dataOut.iterrows():
        row['Percent'] = ''.join(filter(lambda x: x in printable, row['Percent']))
        if type(row['Census']) != int:
            row['Census'] = row['Census'].strip('Est. ')

    dataOut.to_csv(file1, encoding='UTF-8', index=False)

def venue_count_per_city(rv):
    copy1 = getRC2()

    # list format for copy after processing:
    #print(type(rv))

    # make a dataframe for the res types
    res = list(rv['Venue Category'])

    #pprint(copy1)
    #print('\n')

    # this counts the occurance of the restuant type
    mc = 0
    for c in copy1:
        temp = res.count(c[0])
        c[1] += temp
        mc += temp

    # transform into 2 lists
    t1 = [] # category
    c1 = [] # count

    for cc in copy1:
        t1.append(cc[0])
        c1.append(cc[1])

    # turn the list into a DF
    ndf = {
        'Venue Category': t1,
        'Count': c1 # number of occuarances
    }

    out = pd.DataFrame(ndf, columns = ['Venue Category', 'Count'])
    return out, copy1 # returns the dataframe and the list

def getMarket(c1D, c1L): # dataframe, list
    # process non-zeros values
    nonZ = []
    Zs = []

    vc = list(c1D['Venue Category']) # or c1D['Venue Category']
    NoO = list(c1D['Count']) # or c1D['NoO']

    for c in c1L:
        if c[1] != 0:
            nonZ.append(c)
        else:
            Zs.append(c)

    # this is used instead of the total because the non-zeros dont count towards
    # the market share
    marketShare = len(nonZ) 
    per_of_MS = [] # percent of market share

    #print('Cat \t|| Percent')
    for n in c1L:
        temp1 = float((n[1]/marketShare)*100) # convert into a better decimal
        per_of_MS.append(temp1)
        #print("{} || {:.3f}%".format(n[0], temp1))

    # add the list to the DataFrame
    c1D['% of Market'] = per_of_MS

    # add the list to the list
    x = 0
    while x != len(c1L):
        c1L[x].append(per_of_MS[x])
        x += 1

    #print("List:\n")
    #pprint(c1L)

    #print('DF:\n')
    #print(c1D)
    return c1D, c1L


def getRC2():
    RC2 = [
        ['Afghan Restaurant', 0],
        ['American Restaurant', 0],
        ['Asian Restaurant', 0],
        ['BBQ Joint', 0],
        ['Bagel Shop', 0],
        ['Bakery', 0],
        ['Bar', 0],
        ['Beer Bar', 0],
        ['Breakfast Spot', 0],
        ['Brewery', 0],
        ['Bubble Tea Shop', 0],
        ['Burger Joint', 0],
        ['Café', 0],
        ['Cajun / Creole Restaurant', 0],
        ['Chinese Restaurant', 0],
        ['Cocktail Bar', 0],
        ['Coffee Shop', 0],
        ['College Cafeteria', 0],
        ['Creperie', 0],
        ['Cuban Restaurant', 0],
        ['Cupcake Shop', 0],
        ['Deli / Bodega', 0],
        ['Dive Bar', 0],
        ['Doner Restaurant', 0],
        ['Donut Shop', 0],
        ['Ethiopian Restaurant', 0],
        ['Farmers Market', 0],
        ['Fast Food Restaurant', 0],
        ['Fish Market', 0],
        ['Food', 0],
        ['Food & Drink Shop', 0],
        ['Food Truck', 0],
        ['French Restaurant', 0],
        ['Fried Chicken Joint', 0],
        ['Gastropub', 0],
        ['Greek Restaurant', 0],
        ['Hot Dog Joint', 0],
        ['Hotel Bar', 0],
        ['Ice Cream Shop', 0],
        ['Indian Restaurant', 0],
        ['Irish Pub', 0],
        ['Italian Restaurant', 0],
        ['Japanese Restaurant', 0],
        ['Juice Bar', 0],
        ['Mediterranean Restaurant', 0],
        ['Mexican Restaurant', 0],
        ['New American Restaurant', 0],
        ['Noodle House', 0],
        ['Peruvian Restaurant', 0],
        ['Pizza Place', 0],
        ['Portuguese Restaurant', 0],
        ['Pub', 0],
        ['Restaurant', 0],
        ['Salvadoran Restaurant', 0],
        ['Sandwich Place', 0],
        ['Seafood Restaurant', 0],
        ['Southern / Soul Food Restaurant', 0],
        ['Speakeasy', 0],
        ['Steakhouse', 0],
        ['Sushi Restaurant', 0],
        ['Taco Place', 0],
        ['Tex-Mex Restaurant', 0],
        ['Thai Restaurant', 0],
        ['Theme Restaurant', 0],
        ['Vegetarian / Vegan Restaurant', 0],
        ['Vietnamese Restaurant', 0],
        ['Wine Bar', 0]
    ]
    return RC2
