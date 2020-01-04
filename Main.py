import csv
import random  
import datetime

fn = 'data.csv'

with open (fn, 'w') as fp:
    #create csv file
    wr = csv.writer(fp)
    #create the title
    wr.writerow(['Date', 'Sales'])
    #create the vitual data
    startDate = datetime.datetime(2020, 1, 1)
    #create 365 vitual data
    for i in range (365):
        #create a single data, write to csv file
        amount = 300 + i*5 + random.randrange(100)
        wr.writerow([str(startDate),amount])
        #next day
        startDate = startDate + datetime.timedelta(days=1)


import pandas as pd
import matplotlib.pyplot as plt

#read data
df = pd.read_csv('data.csv', encoding = 'cp936')
df = df.dropna()

#create revenue line chart and save to first.jpg
plt.figure()
df.plot (x = df['DATE'])
plt.savefig('first.jpg')

#create monthly bar chart and save to second.jpg
plt.figure()
df1 = df [:]
df1['month'] = df1['DATE'].map(lambda x: x[:x.rindex('-')])
df1 = df1.groupby (by = 'month', as_index = False).sum()
df1.plot(x=df1['month'], kind = 'bar')
plt.savefig('second.jpg')

#find the month with the max increasing rate, write to maxMonth.txt file
plt.figure()
df2 = df1.drop('month', axis = 1).diff()
m = df2['Sales'].nlargest(1).keys()[0]
with open('maxMonth.txt','w') as fp:
    fp.write(df1.loc[m, 'month'])

#create seasonly pie chart and save to third.jpg
plt.figure()
one = df1[:3]['Sales'].sum()
two = df1[3:6]['Sales'].sum()
three = df1[6:9]['Sales'].sum()
four = df1[9:12]['Sales'].sum()
plt.pie([one, two, three, four], labels = ['one', 'two', 'three', 'four'])
plt.savefig('third.jpg')

