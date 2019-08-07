import math
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

print "Initialising"

l = []
x= 0
count = 1
while count <= 10000:
	l.append(2* math.sin(count * x))
	x = 2 * math.pi *25 / 10000
	count = count + 1
plt.plot(l)
plt.show()
count = 1
with open('sine-dataset.csv','wb') as csvfile:
	csvwriter = csv.writer(csvfile)
	for x in l:
		csvwriter.writerow([x])
		count = count + 1
csvfile.close()

print "Sine data write complete"

l = []
x= -1
count = 1
while count <= 10000:
	n = math.exp(x)
	l.append(n)
	x = x + 4.0/10000
	count = count + 1
plt.plot(l)
plt.show()
count = 1
with open('exp-dataset.csv','wb') as csvfile:
	csvwriter = csv.writer(csvfile)
	for x in l:
		csvwriter.writerow([x])
		count = count + 1
csvfile.close()

print "Exponential trend write complete"

df1 = pd.read_csv("sine-dataset.csv", header = None)
df2 = pd.read_csv("exp-dataset.csv", header = None)
df1.columns = ["Value"]
df2.columns = ["Value"]
df_add = df1.add(df2, fill_value=0)
df_add.to_csv("merged-dataset.csv")

df_add.plot(y="Value")
plt.show()

print "Merging the two trends completed"

start = rd.randint(0,1000)

for i in range(0,6):
    increment = 1
    for j in range(start,start+400):
        #df_add["Value"][j] = df_add["Value"][j] + increment
        #increment = increment + 1
        df_add["Value"][j] = df_add["Value"][j] + 5
    start = start + 1500

df_add.plot(y="Value")
plt.show()

print "Seasonal trends incorporated" 

for i in df_add.index:
    j = rd.randint(0,7)
    if j == 0:
        df_add["Value"][i] = df_add["Value"][i] + rd.randint(0,4)
    if j == 1:
        df_add["Value"][i] = df_add["Value"][i] + rd.randint(0,7)
    if j == 2:
        df_add["Value"][i] = df_add["Value"][i] - rd.randint(0,5)

df_add.plot(y="Value")
plt.show()
df_add.to_csv("merged-dataset-with-noise-and-seasonal.csv")

for i in range(0,40):
        j = rd.randint(4000,10000)
        flag = rd.randint(0,3)
        if flag == 1:
                df_add["Value"][j] = df_add["Value"][j] + rd.randint(20,25)
        if flag == 2:
                df_add["Value"][j] = df_add["Value"][j] - rd.randint(20,25)

df_add.plot(y="Value")
plt.show()
df_add.to_csv("merged-dataset-with-noise-seasonal-anomaly.csv")

dt_list = []
dt = datetime.datetime(2019,1,1)
for i in df_add.index:
	dt_list.append(dt)
	dt = dt + datetime.timedelta(minutes=1)
dt_values = pd.Series(dt_list)
df_add_datetime = df_add
df_add_datetime.insert(loc=0, column="Datetime", value= dt_values)
df_add_datetime.to_csv("merged-dataset-with-noise-and-seasonal-anomaly-datetime.csv", index=False)

print "Dataset building finished"
