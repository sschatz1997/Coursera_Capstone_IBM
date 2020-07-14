# functions.py
# system imports
import re
import requests

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
    path = 'E:\\LEARN\\Coursera_Capstone_IBM\\DATA\\'
    file1 = path + "balt_pop.csv"
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
    path = 'E:\\LEARN\\Coursera_Capstone_IBM\\DATA\\'
    file1 = path + "hou_pop.csv"
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
    path = 'E:\\LEARN\\Coursera_Capstone_IBM\\DATA\\'
    file1 = path + "rich_pop.csv"
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
    path = 'E:\\LEARN\\Coursera_Capstone_IBM\\DATA\\'
    file1 = path + "phx_pop.csv"
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
    path = 'E:\\LEARN\\Coursera_Capstone_IBM\\DATA\\'
    file1 = path + 'lat_long.csv'
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

writeCords()