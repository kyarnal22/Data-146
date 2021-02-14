# Project 1

## 1

import pandas as pd
from datetime import datetime

## 2

path_to_data = 'gapminder.tsv'
data = pd.read_csv(path_to_data, sep='\t')

data.describe()
data.shape[0]
data.shape[1]
data.info()
list(data.columns)

## 3

data['year'].unique().tolist()
len(data[(data['year'] == data['year'].max())])
len(data[(data['year'] == 2002)])

## 4

data[(data['lifeExp'] == data['lifeExp'].min())]

## 5
total_gdp = (data['pop'] * data['gdpPercap'])
data['totalGDP'] = total_gdp.tolist()

data_europe2007 = data[(data['continent'] == 'Europe') & (data['year'] == data['year'].max())]
data_fgis2007 = data_europe2007[(data_europe2007['country'] == 'Spain') | (data_europe2007['country'] == 'France') | (
            data_europe2007['country'] == 'Germany') | (data_europe2007['country'] == 'Italy')]
name_gdp = data_fgis2007[['country', 'totalGDP']]
name_gdp.sort_values(by=['totalGDP'], ascending=False)

data_europe2002 = data[(data['continent'] == 'Europe') & (data['year'] == 2002)]
data_fgis2002 = data_europe2002[(data_europe2002['country'] == 'Spain') | (data_europe2002['country'] == 'France') | (
            data_europe2002['country'] == 'Germany') | (data_europe2002['country'] == 'Italy')]
name_gdp = data_fgis2002[['country', 'totalGDP']]
name_gdp.sort_values(by=['totalGDP'], ascending=False)

## 6

data_europe2007 = data[(data['continent'] == 'Europe') & (data['year'] == data['year'].max())]
data_europe2007

(1 + 2 == 3) | (3 > 4)
('cat' == 'dog') ^ (2 > 1)

## 7

data.iloc[1691:1702]
data.iloc[:, 1:4]

## 8

import requests
url = "https://api.covidtracking.com/v1/states/daily.csv"

import os
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

from datetime import datetime as dt
import pytz

file_name_short = 'ctp_' + str(dt.now(tz=pytz.utc)).replace(' ', '_') + '.csv'
file_name = os.path.join(data_folder, file_name_short)

r = requests.get(url)

with open(file_name, 'wb') as f:
    f.write(r.content)

import pandas as pd
df = pd.read_csv(file_name)

## 10

data[["country", "continent", "year", "lifeExp"]]
data.iloc[:, 0:4]


