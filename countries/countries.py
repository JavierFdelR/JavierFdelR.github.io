# Import libraries
import numpy as np # we all know what these does
import pandas as pd
import seaborn as sns
from pandas_datareader import wb # wb es el objeto World Bank connection
import matplotlib.pyplot as plt

color = sns.cubehelix_palette(15, start=.5, rot=-.75, reverse=True)

# Import data
my_indicator = 'NY.GDP.MKTP.CD'
wb_df = wb.download(indicator=my_indicator, country='all', start=2015, end=2015).dropna()[44:]
wb_df = wb_df.sort_values(my_indicator, ascending=False)
x1 = wb_df.index.get_level_values(0).values[0:15]
y1 = wb_df.iloc[:,0].values[0:15]

# Plot 1
plt.figure(1) # va a haber un solo subplot
plt.subplot(121)
plt.bar(range(0,15), y1, color=color, tick_label = x1)
plt.title("Big Countries", fontsize=20)
plt.xticks(rotation=90)
plt.ylabel("GDP (current US$)")

# Import data
my_indicator= 'NY.GDP.MKTP.KD.ZG'
wb_df = wb.download(indicator=my_indicator, country='all', start=2015, end=2015).dropna()[44:]
wb_df = wb_df.sort_values(my_indicator, ascending=False)
x2 = wb_df.index.get_level_values(0).values[0:15]
y2 = wb_df.iloc[:,0].values[0:15]

# Plot 2
plt.subplot(122)
plt.bar(range(0,15), y2, color=color, tick_label = x2)
plt.title('Growing Countries', fontsize=20)
plt.xticks(rotation=90)
plt.ylabel("GDP growth (annual %)")

# Plot Basics
plt.savefig('countries.png')
