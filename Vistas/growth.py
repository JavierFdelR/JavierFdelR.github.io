# Libraries
import pandas_datareader.wb as wb
import numpy as np
import matplotlib.pyplot as plt

# Get data (wb.search('gdp.*capita.*const').iloc[:,:2]) 6.0.GDP_growth
dat = wb.download(indicator='NY.GDP.MKTP.KD.ZG', country=['CL'], start=2000, end=2017)
x = np.array(dat.index.get_level_values(1)).astype(str).astype(int)
y = np.array(dat.values).T[0]

# Plot
plt.figure(1)
plt.subplot(111)
plt.xkcd()
plt.plot(x, y, 'r-', label = 'Chile')
plt.title('GDP')
plt.xlabel('year')
plt.ylabel('GDP growth (annual %)')
plt.legend(loc=1)
plt.xticks(x, rotation=90)
plt.show()
