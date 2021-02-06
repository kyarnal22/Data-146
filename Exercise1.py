
# coding: utf-8

# # Exercise 1

# ## Importing Data & Getting Started

# In[2]:


import pandas as pd


# In[3]:


path_to_data = 'gapminder.tsv'


# In[12]:


data = pd.read_csv(path_to_data, sep = '\t')


# ## 1
# ### Get a list of all the years in this data, without any duplicates. How many unique values are there, and what are they?

# In[16]:


unique_years = data['year'].unique().tolist()
number_of_years = len(unique_years)
print(unique_years)
print(number_of_years)


# ## 2
# ### What is the largest value for population (pop) in this data? When and where did this occur?

# In[18]:


max_pop = data['pop'].max()
max_pop_idx = data['pop'].idxmax()
data.loc[max_pop_idx]


# ## 3
# ### Extract all the records for Europe. In 1952, which country had the smallest population, and what was the population in 2007?

# In[26]:


data_europe = data[data['continent'] == 'Europe']
europe_pop_1952 = data_europe[(data_europe['year'] == data_europe['year'].min())]
min_pop_idx = data_europe['pop'].idxmin()
print(data.loc[min_pop_idx])
iceland_pop_2007 = data[(data['country']=='Iceland') & (data['year'] == data['year'].max())]
iceland_pop_2007

