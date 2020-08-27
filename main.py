import pandas
#import numpy as np
import matplotlib.pyplot as plt
filename = "statistics.csv"
#print(filename)
data=pandas.read_csv(filename)
#print(data) 
years=data.Week
searches=data.fortnite

plt.plot(years,searches)
#plt.xticks(np.arange(0, years+1, 10))

print("this shows the death of fortnite")
plt.xlabel("years")
plt.ylabel("average searches")
plt.title("average fortnite searches vs. years")
plt.show()
# for i in range(0,len(week)):
#   print(week[i])