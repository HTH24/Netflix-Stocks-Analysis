# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:04:28 2020

@author: 胡天行
"""


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head(10))

dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head(10))

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head(10))

# In NFLX and DJI csv files, data is represented by months. In the daily by quarter file, data is represented by days.
# The timelines are different.
# There is an additional column in netflix_stocks_quarterly, and the data reflects daily information, not monthly information.

print(netflix_stocks.head())
netflix_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
dowjones_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
netflix_stocks_quarterly.rename(columns = {'Adj Close': 'Price'}, inplace = True)

print(netflix_stocks.head())

print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


ax = sns.violinplot()
sns.violinplot(data = netflix_stocks_quarterly, x = 'Quarter', y = 'Price')
ax.set_title('Distribution of 2017 Netflix Stock prices by Quarter')
ax.set_xlabel('Closing Stock Price')
ax.set_ylabel('Business Quarters in 2017')
plt.show()

# seems like Q3 is a very steady quarter for NFLX in 2017, there was a lot of upside potential. 
# Q1 and Q4 are relatively more volatile, showing opportunities to speculate



x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]


plt.subplots()
plt.scatter(x_positions, earnings_actual, color = 'red', alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, color = 'blue', alpha = 0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels, rotation = 30)
plt.title('Earnings Per Share in Cents')
plt.show()

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]

plt.subplots()
plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars2_x, earnings_by_quarter)

plt.title('Earnings and Revenue reported by Netflix in 2017\'s 4 quarters')


middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.legend(labels)
plt.xticks(middle_x, quarter_labels)


# Left plot Netflix
# f = plt.figure(figsize = (20, 20))


plt.subplots()
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xticks(range(len(netflix_stocks['Date'])))
ax1.set_xticklabels(netflix_stocks['Date'], rotation = 90)
ax1.set_ylabel('Stock Price')




# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_xticks(range(len(dowjones_stocks['Date'])))
ax2.set_xticklabels(dowjones_stocks['Date'], rotation = 90)
ax2.set_title('Dow Jones')
plt.subplots_adjust(wspace = 0.5)
plt.show()