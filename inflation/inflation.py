# Libraries
import pandas_datareader.wb as wb
import numpy as np
import matplotlib.pyplot as plt

# Get data (wb.search('gdp.*capita.*const').iloc[:,:2]) 6.0.GDP_growth
dat = wb.download(indicator='NY.GDP.DEFL.KD.ZG', country=['US','CN','JP','DE','GB'], start=2000, end=2017)
x = np.array(dat.index.get_level_values(1)).astype(int)

my_countries = dat.index.levels[0].values
x = dat.loc[my_countries[0]].index.get_level_values(0).values.astype(int)

# Plot
plt.figure(1)
for i in range(0,len(my_countries)):
    plt.subplot(111)
    y = dat.loc[my_countries[i]].values.flatten()
    plt.plot(x, y, label = my_countries[i])
plt.title('Inflation', fontsize=19)
plt.xlabel('year')
plt.ylabel('GDP deflator (annual %)')
plt.legend(loc=1)
plt.xticks(x, rotation=90)
plt.savefig('inflation.png')
