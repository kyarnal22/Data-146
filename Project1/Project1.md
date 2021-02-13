# Project 1

## 1 

A package is a group of Python modules that, when imported into your Python workspace allow for the use of various commands that would otherwise require more effort to complete. 
Within each package are a series of libraries that each have a specific function relating to the main package.
To install a package and then a library, you must first make sure the package is installed within the Python interpreter - found under Preferences in PyCharm. If it is not installed, a package can be easily found by typing in its name and adding it to the interpreter.
Once the package is installed, you then have to import it into the workspace with a line of code. 

`import pandas as pd` 

This would import the pandas library into your workspace under an alias 'pd'. Using an alias can be helpful in keeping code short and easy to read.

`import datetime from datetime`

This would import the datetime function from the datetime library. This is helpful when you only need access to a certain function from within a library; rather than importing the entire library, you can import certain functions specifically. 

## 2

A data frame is a pandas structure that allows for the reading of data sets by organizing data entries into a table of columns and values. 
When working with dataframes, the pandas library is particularly helpful as it allows for the reading of the data in addition to data subsetting and manipulation.
To read a file in its remote location in your file system, you would need to write a read_() command, specifying the library you are using and the path to the file. The pandas library has already been imported under an alias, so the code used would look something like this:

`path_to_data = 'gapminder.tsv'`
`data = pd.read_csv(path_to_data, sep = '\t')`

The dataset we're working this is tab-separated; however the pandas library will assume it is a comma-separated file. To get around this, within the read() command, specify that you want data read as a csv file, read_csv(), while
including that the data is tab-separated, sep = '\t'. 

To return a description of the data, use the describe() command:

`data.describe()`

To determine how many rows and columns are included in the dataset, use the .shape() command.

`data.shape()`

To get a summary of the names of the columns, use data.info(), or data.columns() as a list:

`data.info()`
`list(data.columns)`

## 3 

Starting in 1952, the years come in five-year increments. To make it more current, data from 2012 and 2017 should be included, adding 142 records for each year to the data frame - 284 in total.

## 4

In this data frame, the lowest life expectancy occured in Rwanda in 1992, where life expectancy was about 23 years. This was around the time of the Rwanda genocide, when up to a million people were killed. This, in addition to the nation's poor health at the time was likely the biggest factor in driving down average life expectancy. 

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

Spain experienced the greatest increase in total GDP between 2002 and 2007, increasing from .97 trillion USD to 1.16 trillion USD, 

## 6

The '&' symbol is used to represent 'and' and would be used in cases where you are looking for data that has both of the given criteria. The '==' symbol is used for checking if a variable is equal to a certain value in conditional statements. Using a single equal sign would only be appropriate when assigning values to a variable name. The following code would return values where country is equal to Europe and the year is equal to 2007.

`data_europe2007 = data[(data['continent']=='Europe') & (data['year'] == data['year'].max())]`

The '|' symbol is used to represent 'or' and would return True as long as at least one of the given arguments is True. The following code will return True even though 3 is not greater than 4, because it is only asking if one of the given arguements is correct.

`(1+2 == 3) | (3 > 4)`

The '^' symbol is used to represent an exclusive or. It will return True if one argument is True and the other False, but will return False if both are True or both are False. The following will return False as both are False.

`('cat' == 'dog') ^ (2 > 1)`

## 7 

Describe the difference between .loc and .iloc. Provide an example of how to extract a series of consecutive observations from a data frame. Stretch goal: provide an example of how to extract all observations from a series of consecutive columns.
## 8 

Describe how an api works. Provide an example of how to construct a request to a remote server in order to pull data, write it to a local file and then import it to your current work session.
## 9 

Describe the apply() function from the pandas library. What is its purpose? Using apply) to various class objects is an alternative (potentially preferable approach) to writing what other type of command? Why do you think apply() could be a preferred approach?
## 10

Also describe an alternative approach to filtering the number of columns in a data frame. Instead of using .iloc, what other approach might be used to select, filter and assign a subset number of variables to a new data frame?

