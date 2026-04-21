import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/LU/IBI1_2025-26/Practical 10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.iloc[0:10,2:4])
# 1998 reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan.
my_columns = dalys_data["Entity"] == "Zimbabwe"
print(dalys_data.loc[my_columns,"Year"])
# the first 1990 and last year 2019 for which these data were recorded.
recent_data = dalys_data.loc[dalys_data.Year == 2019]
largest = recent_data.DALYs.max()
smallest = recent_data.DALYs.min()
largest_row = recent_data[recent_data.DALYs==largest]
smallest_row = recent_data[recent_data.DALYs==smallest]
largest_country = largest_row.Entity.iloc[0]
smallest_country = smallest_row.Entity.iloc[0]
print(smallest_country," reported the smallest DALYs values in the most recent year for which data are available (2019)")
print(largest_country," reported the largest DALYs values in the most recent year for which data are available (2019)")
# the maxium name is Lesotho, the minimum name is Singapore.
singapore = dalys_data.loc[dalys_data.Entity == "Singapore"]
plt.plot(singapore.Year,singapore.DALYs,'b+')
plt.xticks(singapore.Year,rotation=-90)
plt.xlabel("year")
plt.ylabel("DALYs")
plt.title("DALYs of Singapore over time")
plt.show()
top = recent_data.nlargest(10,"DALYs")
countries = top.Entity
DALYs = top.DALYs
plt.pie(DALYs,labels=countries,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title("the distribution of DALYs across countries which have top 10 DALYs in 2019")
plt.show()