countries = [{'name':"UK", 'pop20':66.7, 'pop24':69.2}, {'name':"China",'pop20':1426, 'pop24':1410}, {'name':"Italy", 'pop20':59.4, 'pop24':58.9}, {'name':"Brazil", 'pop20':208.6, 'pop24':212.0}, {'name':"USA", 'pop20':331.6, 'pop24':340.1}]
#calculate the percentage change of each population
for country in countries:
    per_change = ((country['pop24'] - country['pop20'])/ country['pop20'])*100
    country['perchange'] = per_change
print("The percentage population change for each country (2020~2024):")
for c in countries:
    print(c['name'],":",c['perchange'],"%")
#put in descending order
sorted_countries = sorted(countries, key=lambda x: x['perchange'], reverse=True)
print("Population changes in descending order:")
for i in sorted_countries:
    print(i['name'],":", i['perchange'],"%")
maxin = sorted_countries[0]
maxde = sorted_countries[-1]
print("Country with the largest population increase:", maxin['name'])
print("Country with the largest population decrease:", maxde['name'])

#bar chart
import matplotlib.pyplot as plt

names = [i['name'] for i in sorted_countries]
changes = [i['perchange'] for i in sorted_countries]

plt.bar(names, changes)
plt.title("The Population Percent Change in 5 Countries (2020~2024)")
plt.xlabel("Country")
plt.ylabel("Percent Change (%)")
plt.show()