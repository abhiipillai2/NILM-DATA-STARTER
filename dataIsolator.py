import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#reading data from csv file
dataset = pd.read_csv("dcsub002.csv",parse_dates =["time"])

print (dataset.index)

#setting index as timestamp
dataset.set_index('time',inplace=True) 
dataset.index= pd.to_datetime(dataset.index)

#cutting the spesif time stamp
dataset = dataset['05-11-2022 19:11:00':'05-11-2022 20:20:00']

print (dataset)

#Assigning x and y values to variable
x = dataset.index
y = dataset["power"].values

#ploting the graph
plt.plot(x,y ,label = "mains reading")
# plt.plot(time,result ,label = "model predicted value of refrigerator")
# plt.plot(time,yy ,label = "actual value of refrigerator")
# plt.legend()
plt.show()