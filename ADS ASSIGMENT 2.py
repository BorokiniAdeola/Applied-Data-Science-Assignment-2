# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""
Creating a def function to read in our datasets and returns  two 
dataframes:one with years as columns, the other with nations
"""

def read_data (filename, **others):
    """
    A function that reads in climate change data alongside various indicators from 
    the world bank database and returns both the original and transposed version of
    the dataset
    
    Args:
        filename: the name of the world bank data that will be read for analysis 
        and manupulation
        
        **others: other arguments to pass into the functions as need be
            
    Returns: 
        The original dataset format as obtained from the world bank and its transposed version
    """        

    # Reading in the climate dataset for to be used for analysis with years as columns
    climate_data = pd.read_csv(filename, skiprows=4) 
    
    # Transposing and cleaning the dataset such that the country names are the columns
    climate_data2 = pd.DataFrame.transpose(climate_data)
    climate_data2=climate_data2.drop(['Country Name','Country Code','Indicator Code'])
    climate_data2.columns=climate_data2.iloc[0]
    climate_data2=climate_data2.iloc[1:]
    
    return climate_data, climate_data2

# Reading in our datasets for analysis
climate_data, climate_data2 = read_data(r"C:\Users\Admin\Desktop\WORLD_BANK_DATA.csv")
print(climate_data)
print(climate_data2)

# For this analysis, we will make do with 4 indicators of choice
indicators=climate_data[climate_data['Indicator Name'].isin(['Arable land (% of land area)','Urban population',
                                                  'CO2 emissions (kt)','Electric power consumption (kWh per capita)'])]

indicators.head()

"""
The data looks complex and uneasy to work with, 
various data wrangling exercise will be perform to make the data accessible and easier to analyze
"""
climate_data=pd.DataFrame.transpose(indicators) # Transposing the data
print(climate_data)

# Making the country name as columns.
climate_data.columns=climate_data.iloc[0]
climate_data

# dropping rows not needed from the data
climate_data=climate_data.drop(['Country Name','Country Code','Indicator Code'])
climate_data

"""
For this analysis, 7 countries of choice across various continents
will be picked 
"""
# Selecting countries for analysis
countries= climate_data[['China', 'Nigeria', 'India','Philippines','United States', 'Germany','Brazil']]

countries

# Checking for missing values
countries.isnull().mean() # We have losts of missing values, some columns having 50% of its values missing

# dropping all missing values from our datasets
countries.dropna(inplace=True)
countries.head()
countries.index
countries

"""
for further accessibilty and ease of data analysis, datasets that combines all 
countries on each indicator will be created in five years increments from 1990 to 2010
"""
# Creating a dataframe for all selected countries on Urban population
urban_pop=countries.iloc[[1,6,11,16,21],[0,4,8,12,16,20,24]] 
urban_pop=urban_pop.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
urban_pop.index=pd.to_numeric(urban_pop.index) # converting index values to numeric format
urban_pop

# creating a dataframe for all selected countries on c02 emission
co2= countries.iloc[[1,6,11,16,21],[1,5,9,13,17,21,25]] 
co2=co2.apply(pd.to_numeric)  # converting to data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
co2

# creating a dataframe for all selected countries on electric consumption 
electric=countries.iloc[[1,6,11,16,21],[2,6,10,14,18,22,26]]
electric=electric.apply(pd.to_numeric)  # converting to data type to a numeric format
co2.index=pd.to_numeric(co2.index) # converting index values to numeric format
electric

# creating a dataframe for all selected countries on Arable land
arable=countries.iloc[[1,6,11,16,21],[3,7,11,15,19,23,27]]
arable=arable.apply(pd.to_numeric)# converting the data type to a numeric format
arable.index=pd.to_numeric(arable.index) # converting index values to numeric format
arable.head()

"""
Statistical overview for the urban population across selected countries.
Applying Statistical function for the four selected indicators 
across the 7 picked countries.
"""
#statistical function for urban population
print(urban_pop.describe())
print(urban_pop.mean()) # checking the mean urban population
print(urban_pop.median()) # checking the median urban population
print(urban_pop.std()) # checking the urban population standard deviation

#Statistical function for c02 emission
print(co2.describe())
print(co2.mean()) # checking the mean co2
print(co2.median()) # checking the median co2
print(co2.std()) # checking the co2 standard deviation

#Statistical function for electric consumption 
print(electric.describe())
print(electric.mean()) # checking the mean co2
print(electric.median()) # checking the median co2
print(electric.std()) # checking the co2 standard deviation
plt.style.available

"""
Plotting a grouped bar of CO2 emission for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""
plt.style.use('default')
co2.T.plot(kind='bar')
plt.title(' nations co2 emission in 5 years increments')
plt.xlabel('Countries')
plt.ylabel('Co2 emission (kt)')
plt.show()



"""
Plotting a grouped bar of urban population for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""
plt.style.use('default')
co2.T.plot(kind='bar')
plt.title(' urban population in 5 years increments')
plt.xlabel('Countries')
plt.ylabel('Urban Population')
plt.show()

"""
Plotting a line plot of urban population for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""
plt.figure(figsize=(10,6))
plt.style.use('default')
urban_pop.plot()
plt.title('Urban Population Trend for The 7 countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.xticks([1990,1995,2000,2005,2010])
plt.show()

"""
Plotting a line plot of nations c02 emission for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""
plt.figure(figsize=(10,6))
plt.style.use('default')
urban_pop.plot()
plt.title('nations c02 emission for the 7 nations')
plt.xlabel('Year')
plt.ylabel('Co2 emmision (kt)')
plt.xticks([1990,1995,2000,2005,2010])
plt.show()

"""
Plotting a scatter plot to show relationship for Urban poulation and co2 emission for United States
"""
plt.style.use('ggplot')
plt.scatter(urban_pop['United States'], co2['United States'])
plt.title('Relationship between Urban population and co2 emission for United States')
plt.xlabel('Urban population')
plt.ylabel('co2 emission')
plt.show()
