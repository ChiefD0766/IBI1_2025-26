import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/cygwin64/home/26838/IBI/IBI_25-26/IBI1_2025-26/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# show the third and fourth columns (the year and the DALYs) for the first 10 rows (inclusive)
print("\n The year and the DALYs for the first 10 rows")
print(dalys_data.iloc[0:10, 2:4])

# Answer1: Year 1998 reported the maximum DALYs across the first 10 years in Afghanistan

# fnd every row where the Entity is “Zimbabwe”
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[is_zimbabwe]
zimbabwe_years = zimbabwe_data["Year"]
print("\n Data of Zimbabwe")
print(zimbabwe_years)

# Answer2: The first year recorded is 1990; the last year recorded is 2019

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

max_country = recent_data.loc[recent_data["DALYs"].idxmax(), "Entity"]
min_country = recent_data.loc[recent_data["DALYs"].idxmin(), "Entity"]
# new-learnt: idxmax/idxmin: functions from panda, to find the row index corresponding to the maximum/minimum value in a certain column
print("\nThe country with the maximum DALYs in 2019:", max_country)
print("The country with the minimum DALYs in 2019:", min_country)

# plot example: Singapore, the country with the minimum DALYs in 2019
country = dalys_data.loc[dalys_data["Entity"] == min_country]
plt.plot(country["Year"], country["DALYs"], 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("Overtime DALYs in " + min_country)
plt.xticks(country["Year"], rotation=-90)
plt.show()

# Solution of my question
dalys_00upper = dalys_data[dalys_data["Year"] >= 2000]
dalys_00_06 = dalys_00upper[dalys_00upper["Year"] <= 2006]
medians = dalys_00_06.groupby("Year")["DALYs"].median() # "groupby" learned from highschool python class
print("\n Global Median DALYs (2000-2006) - SARS Context Analysis ")
for year in range(2000, 2007):
    print(f"Global Median DALYs in {year}: {medians[year]}")
plt.plot(medians.index, medians.values, 'b-o', label='Global Median DALYs')
plt.scatter(2003, medians[2003], color='red', s=80, label='2003 (SARS Outbreak)')
plt.xlabel("Year")
plt.ylabel("Global Median DALYs Rate")
plt.legend()
plt.title("Global Median DALYs Rate (2000-2006) - SARS Impact Analysis")
plt.show()

