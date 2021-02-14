# Project 1

## 1 

A package is a group of Python modules that, when imported into your Python workspace allow for the use of various, helpful commands. Within each package are a series of libraries that each have a specific function relating to the main package. To install a package and library, you must first make sure the intended package is installed within the Python interpreter - found under Preferences in PyCharm. If it is not installed, a package can be easily found by typing in its name and adding it to the interpreter. Once the package is installed, you then have to import it into the workspace with a line of code. 

`import pandas as pd` 

This would import the pandas library into your workspace under an alias 'pd'. Using an alias can be helpful in keeping code short and easy to read.

`from datetime import datetime`

This would import the datetime function from the datetime library. This is helpful when you only need access to a certain function from within a library; rather than importing the entire library, you can import certain functions specifically. 

## 2

A data frame is a structure that allows for the reading of data sets by organizing data entries into a table of columns and values. When working with dataframes, the pandas library is particularly helpful as it allows for the reading of the data in addition to data subsetting and manipulation. To read a file in its remote location in your file system, you would need to write a `read_()` command, specifying the library you are using and the path to the file. The pandas library has already been imported under an alias, so the code used would look something like this:

`path_to_data = 'gapminder.tsv'`
`data = pd.read_csv(path_to_data, sep = '\t')`

The dataset we're working this is tab-separated; however the pandas library will assume it is a comma-separated file. To get around this, within the `read_()` command, specify that you want data read as a csv file, `read_csv()`, while including that the data originally was tab-separated, `sep = '\t'`. 

To return a description of the data, use the `describe()` command:

`data.describe()`

To determine how many rows and columns are included in the dataset, use the .shape() command.

`data.shape[0]`
`data.shape[1]`

There are 1704 rows and 6 columns in this dataframe. To get a summary of the names of the columns, use `data.info()`, or `data.columns()` as a list:

`data.info()`
`list(data.columns)`

## 3 

Starting in 1952, the years come in five-year increments. To make it more current, data from 2012 and 2017 should be included, adding 142 records for each year to the data frame - 284 in total.

## 4

In this data frame, the lowest life expectancy occured in Rwanda in 1992, where life expectancy was about 23 years. This was around the time of the Rwanda genocide, when up to a million people were killed. This, in addition to the nation's poor public health at the time was likely the biggest factor in driving down average life expectancy. 

## 5 

In 2007, total GDP for Germany, France, Italy, and Spain were as follows: 

| Country  | Total GDP |
| ------------- | ------------- |
| Germany  | 2.65 trillion  |
| France  | 1.86 trillion  |
| Italy  | 1.66 trillion | 
| Spain  | 1.16 trillion |

In 2002, total GDP for Germany, France, Italy, and Spain were as follows: 

| Country  | Total GDP |
| ------------- | ------------- |
| Germany  | 2.47 trillion  |
| France  | 1.73 trillion  |
| Italy  | 1.62 trillion | 
| Spain  | .97 trillion |

Spain experienced the greatest increase in total GDP between 2002 and 2007, increasing from .97 trillion USD to 1.16 trillion USD.

## 6

The '&' symbol is used to represent 'and' and would be used in cases where you are looking for data that has both of the given criteria. The '==' symbol is used for checking if a variable is equal to a certain value in conditional statements. Using a single equal sign would only be appropriate when assigning values to a variable name. The following code would return values where country is equal to Europe and the year is equal to 2007.

`data_europe2007 = data[(data['continent']=='Europe') & (data['year'] == data['year'].max())]`

The `|` symbol is used to represent 'or' and would return True as long as at least one of the given arguments is True. The following code will return True even though 3 is not greater than 4, because it is only asking if one of the given arguements is correct.

`(1+2 == 3) | (3 > 4)`

The '^' symbol is used to represent an exclusive or. It will return True if one argument is True and the other False, but will return False if both are True or both are False. The following will return True as 2 > 1 but cat is not equal to dog.

`('cat' == 'dog') ^ (2 > 1)`

## 7 

The .loc command is a location command used to extract a row of data when given its index label as a parameter. The .iloc works similarly but returns a row by it's integer position in the dataset rather than its index label. The following code will return all rows of data between the integer positions 1691 and 1702, not including entry 1702.

`data.iloc[1691:1702]`

The following code will return all observations from the second, third, and fourth columns. 

`data.iloc[:, 1:4]`


## 8 

An api is an Application Programming Interface, and it a part of a website's remote server that receives and processes requests. It allows different applications to work together.

To pull data from a remote server, you first have to send a request using the requests library.

`import requests`

You then must specify where the data is coming from in a url. 

`url = "https://api.covidtracking.com/v1/states/daily.csv"`

Then you can write it to a local file in a folder on your server using the os library.

`import os`

`data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)`
    
After setting a filename for your data, you can retrieve the data from the request and populate your new file.
 
`from datetime import datetime as dt`
`import pytz`
 
`file_name_short = 'ctp_' + str(dt.now(tz = pytz.utc)).replace(' ', '_') + '.csv'`

`file_name = os.path.join(data_folder, file_name_short)`

`r = requests.get(url)`

`with open(file_name, 'wb') as f:
    f.write(r.content)`
    
 Once your file is written, you cna import it into your workspace using pandas.
    
`import pandas as pd`
`df = pd.read_csv(file_name)`

## 9 

The apply() function from the pandas library allows for the user to take any function and apply it to all values in the given series. For example, the apply() function could be used to sum all values for a particular column. Using apply() could be an alternative to writing out an actual function and then having to execute it across all series objects, which could lower output speed and efficiency, while taking up more space and increasing the chance of making a mistake. 

## 10

Instead of using .iloc to filter columns, you could just make a new subset of your data frame. The following two lines of code return the same output; however, using the first option is potentially easier and allows both consecutive and non-consecutive columns to be extracted by name. 

`data[["country", "continent", "year", "lifeExp"]]`
`data.iloc[:, 0:4]`

[Project 1 Jupyter Notebook](Project1.ipynb)

[Project 1 File](Project1.py)
