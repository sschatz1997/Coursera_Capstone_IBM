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

writePhoenixPopulation()