# Libraries
import pandas_datareader.wb as wb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Get data
# GDP (current US$) (NY.GDP.MKTP.CD)
# GDP per capita (current US$) (NY.GDP.PCAP.CD)
dat = wb.download(indicator=['NY.GDP.PCAP.CD','NY.GDP.MKTP.CD'], country=['CL','GB'], start=2000, end=2017) # GDP per capita (current US$)
chile_per = dat['NY.GDP.PCAP.CD'].loc['Chile'].pct_change()
chile_tot = dat['NY.GDP.MKTP.CD'].loc['Chile'].pct_change()
uk_per = dat['NY.GDP.PCAP.CD'].loc['United Kingdom'].pct_change()
uk_tot = dat['NY.GDP.MKTP.CD'].loc['United Kingdom'].pct_change()



# Plot
plt.figure(1)
plt.subplot(211)
plt.plot(chile_per,'r-', label='GDP per capita: Chile')
plt.plot(chile_tot,'r--', label='GDP: Chile')
plt.subplot(212)
plt.plot(chile_per - chile_tot,'r--', label='Chile')
plt.plot(uk_per - uk_tot,'b-', label='United Kingdom')


# Plot parameters
plt.title("Gap between GDP and GDP per capita")
plt.xlabel("year")
plt.ylabel("GDP per capita - GDP total \n (yearly USD variation)")
plt.legend(loc=1)

plt.show()

#print(dat)
