
### Import libraries

import numpy as np # we all know what these does
import pandas as pd
import pycountry # for a list of all countries
from pandas_datareader import wb # wb es el objeto World Bank connection
import matplotlib.pyplot as plt


gdp = wb.download(indicator='NY.GDP.MKTP.CD', country='all', start=2015, end=2015).dropna()

#List of all countries names
paises = list(pycountry.countries)
all_country_names = []
for i in range(1,len(pycountry.countries)):
    all_country_names.append(paises[i].name)

#List of all countries names
indice = gdp.index
wb_country_names = indice.get_level_values(0)

#Interception
available_countries = list(set(all_country_names) & set(wb_country_names))

### Get only the Serie Im looking for
data = gdp.ix[available_countries]
a = data['NY.GDP.MKTP.CD']
b = a.groupby(level=0).mean()
c = b.sort_values(ascending=False)

### Clean and organize data
# Structre to data (dat.info(), dat.index, dat.shape)
x = np.array(gdp.index.get_level_values(1)).astype(str).astype(int)
y = np.array(gdp.values)

### Plot data
%debug
print(c)
