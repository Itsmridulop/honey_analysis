import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# getting info about the data
honeyData = pd.read_csv(r'./US_honey_dataset.csv')
print('top rows\n',honeyData.head(4))
print('botton rows\n',honeyData.tail(4))
print('shape\n', honeyData.shape)
print('info\n', honeyData.info())
print('describe\n', honeyData.describe())
print('null value\n', honeyData.isnull().sum())
print('Duplicate value\n', honeyData.duplicated().sum())
print('number of unique value\n', honeyData.nunique())

# data cleaning
cleanedData = honeyData.drop(columns=['Unnamed: 0'])
print('top rows of cleaned data\n',cleanedData.head())

# no duplicate and null values in the data so we don't need to do anything
# if numbers of rows having null value > 30% of data then we have to fill the null value with mean or median or mode
# if numbers of rows having null value < 30% of data then we have to drop the
# if we have duplicate values then we have to drop the duplicate values by drop_duplicate()

# Q1. which states are rarely contributing for honey production since last 27 years?

lst_states = cleanedData['state'].value_counts().index
lst_vals = cleanedData['state'].value_counts().values

plt.figure(figsize=(10,10))
plt.pie(lst_vals, labels=lst_states, autopct='%.2f%%')
plt.show()


# Q2. which states are contributing for honey production since last 27 years?
grouped_data = cleanedData.groupby('state')['production'].sum().reset_index().sort_values(by='production', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(data=grouped_data, x='state', y='production')
plt.xticks(rotation=90)
plt.show()


# Q3. What is the Change in mean Average price of Honey from 1995 to 2021, observe the trend.
print('mean of average price\n', cleanedData['average_price'].mean())

# Which was the year when production of Honey in entire US was the highest?
grouped_data_year = cleanedData.groupby('year')['production'].sum().reset_index().sort_values(by='production', ascending=False)
plt.figure(figsize=(10,10))
sns.barplot(data=grouped_data_year, x='year', y='production')
plt.xticks(rotation=90)
plt.show()


# Q5.from the above inference we get the production was highest in the year 2000, now lets infer
# which state was having highest contribution in that year?
grouped_data_2000 = cleanedData[cleanedData['year'] == 2000]
plt.figure(figsize=(10,10))
sns.barplot(data=grouped_data_2000, x='state', y='production')
plt.xticks(rotation=90)
plt.show()


# Q6.Which states are having the highest no. of colonies in year 2010
grouped_data_2010 = cleanedData[cleanedData['year'] == 2010]
plt.figure(figsize=(10,10))
sns.barplot(data=grouped_data_2010, x='state', y='colonies_number')
plt.xticks(rotation=90)

plt.show()