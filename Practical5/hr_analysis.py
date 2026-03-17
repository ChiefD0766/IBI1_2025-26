import numpy as np
import matplotlib.pyplot as plt

#stating how many patients are in the dataset and the mean heart rate
hr = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
patnum = len(hr)
mean_hr = np.mean(hr)
print("There are", patnum, "patients in the dataset, and the average heart rate is", mean_hr, "/bpm")

#categorize
low = 0
normal = 0
high = 0
for i in hr:
    if i < 60:
        low += 1
    if 60 <= i <= 120:
        normal += 1
    if i > 120:
        high += 1
hr_ctgr = {'low':low, 'normal':normal, 'high':high}
print("Patient number in catagories---low heart rate:",low, "normal heart rate:", normal, "high heart rate:",high)
max_ctgr = max(hr_ctgr, key=hr_ctgr.get)
print("The",max_ctgr, "heart rate category contains the largest number of patients.")

#pie chart
categories = list(hr_ctgr.keys())
num = list(hr_ctgr.values())
colors = ['lightcoral', 'lightgreen','lightblue']
plt.pie(num, labels = categories, colors = colors, startangle=90)
plt.title('Distributions of Heart Rate Categories')
plt.show()
