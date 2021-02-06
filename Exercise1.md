# Exercise 1

## Importing and Reading Data

 `import pandas as pd`
 
`path_to_data = 'gapminder.tsv'`

`data = pd.read_csv(path_to_data, sep = '\t')`

## 1
### Get a list of all the years in this data, without any duplicates. How many unique values are there, and what are they?
`unique_years = data['year'].unique().tolist()`

`number_of_years = len(unique_years)`

There are 12 unique years in the dataset: 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007

## 2 
### What is the largest value for population (pop) in this data? When and where did this occur?

`max_pop = data['pop'].max()`

`max_pop_idx = data['pop'].idxmax()`

`data.loc[max_pop_idx]`

The largest population value is 1,318,683,096, which occured in China in 2007.

## 3
### Extract all the records for Europe. In 1952, which country had the smallest population, and what was the population in 2007?¶

`data_europe = data[data['continent'] == 'Europe']`

`europe_pop_1952 = data_europe[(data_europe['year'] == data_europe['year'].min())]`

`min_pop_idx = data_europe['pop'].idxmin()`

`iceland_pop_2007 = data[(data['country']=='Iceland') & (data['year'] == data['year'].max())]`

In 1952, the European country with the smallest population was Iceland. In 2007, Iceland had a population of 301,931.
