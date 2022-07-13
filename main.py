# -*- coding:utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
import cssselect
import lxml.html
from pprint import pprint
import re
import html
import numpy as np
import string

headers = {"Accept-Language": "en-US, en;q=0.5"}
IMDB_TV = "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"
Rotten_TV = "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular?page=1"
response_IMDB = requests.get(IMDB_TV)
response_Rotten = requests.get(Rotten_TV)
print(response_Rotten, response_IMDB)
soup_IMDB = BeautifulSoup(response_IMDB.content, 'html.parser')
soup_Rotten = BeautifulSoup(response_Rotten.content, 'html.parser')

tree = lxml.html.fromstring(response_Rotten.text)
links = tree.cssselect('a') #or tree .xpath('//a')
IMDB_movie_name = []
IMDB_rating = []
IMDB_metaScore = []

Rotten_movie_name = []
Rotten_rating = []
Rotten_metaScore = []

IMDB_TV_Data = soup_IMDB.findAll('div', attrs = {'class': 'lister'})

for store in IMDB_TV:
    name = store.find('div')['href']
    IMDB_movie_name.append(name)

#    year_of_release = store.find('span', class = 'secondaryInfo').text.replace('(', '').replace(')', '')
#    IMDB_year.append(year_of_release)
#    print(year_of_release)
