# -*- coding: utf-8 -*-
"""data-cleaning-round-2-smartphones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E7nUdvyKpm6C-4oIw67rV6EufLEeCTrx
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)

df = pd.read_csv('smartphone_cleaned_v.csv')

df.shape

df.head()

df.info()

df.isnull().sum()

# brand name
df['brand_name'].value_counts()

df[df['price']>200000]

df['price'].isnull().sum()

df['processor_brand'] = df['processor_brand'].str.replace('sanpdragon','snapdragon')
df['processor_brand'] = df['processor_brand'].str.replace('apple','bionic')
df['processor_brand'] = df['processor_brand'].str.replace('samsung','exynos')

temp_df = df[df['processor_brand'] == 'qualcomm']

df.loc[temp_df.index, 'processor_brand'] = 'snapdragon'

temp_df = df[df['processor_brand'] == 'a13']

df.loc[temp_df.index, 'processor_brand'] = 'bionic'

df['processor_brand'].value_counts()

df[df['processor_brand'].isnull()]

df['num_cores'].value_counts()

df['processor_speed'].describe()

def fast(row):

  if row['fast_charging'] == -1:
    return 0
  else:
    return 1

df.columns

x = df.apply(fast,axis=1)
df.insert(12,'fast_charging_available',x)

df['fast_charging'] = df['fast_charging'].apply(lambda x:np.nan if x == 0 or x == -1 else x)

df.head()

df['ram_capacity'].value_counts()

temp_df = df[df['internal_memory'].isnull()]

df.loc[temp_df.index,['ram_capacity','internal_memory']] = [[4,64],[4,64]]

df['internal_memory'].value_counts()

df['screen_size'].describe()

sns.displot(kind='kde',data=df,x='screen_size')

df['screen_size'].skew()

sns.boxplot(df['screen_size'])

df['extended_memory'].value_counts()

df['extended_memory_available'] = df['extended_memory'].apply(lambda x:0 if x == '0' else 1)

def extended_extractor(row):

  if row['extended_memory_available'] == 0:
    return np.nan
  else:
    if row['extended_memory'] == '1 TB':
      return 1024
    elif row['extended_memory'] == '512 GB':
      return 512
    elif row['extended_memory'] == '256 GB':
      return 256
    elif row['extended_memory'] == 'Not Specified':
      return np.nan
    elif row['extended_memory'] == 'Memory Card (Hybrid)':
      return np.nan
    elif row['extended_memory'] == '128 GB':
      return 128
    elif row['extended_memory'] == '2 TB':
      return 2048
    elif row['extended_memory'] == '32 GB':
      return 32
    elif row['extended_memory'] == '64 GB':
      return 64
    elif row['extended_memory'] == '1000 GB':
      return 1000

def extended_extractor(row):

  if row['extended_memory_available'] == 0:
    return np.nan
  else:
    if row['extended_memory'] == 'Not Specified':
      return np.nan
    elif row['extended_memory'] == 'Memory Card (Hybrid)':
      return np.nan
    else:
      return row['extended_memory']

df['extended_memory']

x = df.apply(extended_extractor,axis=1).str.replace('\u2009',' ').str.split(' ').str.get(0)

df['extended_memory_available']

df['extended_upto'] = x

df['extended_upto'].value_counts()

def transform(text):

  if text == '1':
    return '1024'
  elif text == '2':
    return '2048'
  elif text == '1000':
    return '1024'
  else:
    return text

df['extended_upto'] = df['extended_upto'].apply(transform)

df['os']

def os_transform(text):

  if 'Memory' in text:
    return np.nan
  elif 'android' in text:
    return text
  elif 'ios' in text:
    return text
  else:
    return 'other'

df['os'] = df['os'].apply(os_transform)

df.head()

df['extended_upto'].value_counts()

df.drop(columns=['processor_name','extended_memory'],inplace=True)

df.isnull().sum()

df.corr()['rating']

df.info()

df['primary_camera_front'].value_counts()

df['primary_camera_front'] = df['primary_camera_front'].apply(lambda x: np.nan if x == 'Main' else x).astype(float)

df['num_cores'].value_counts()

df['num_cores'] = df['num_cores'].str.replace('Octa Core','8')
df['num_cores'] = df['num_cores'].str.replace('Hexa Core','6')
df['num_cores'] = df['num_cores'].str.replace('Quad Core','4')

df.to_csv('smartphone_cleaned_v4.csv',index=False)

new_df = pd.read_csv('smartphone_cleaned_v4.csv')

new_df[['brand_name','model','processor_brand']]

new_df['num_cores'] = new_df['num_cores'].astype(str)

new_df['num_cores'] = new_df['num_cores'].str.replace('Octa Core','8')
new_df['num_cores'] = new_df['num_cores'].str.replace('Hexa Core','6')
new_df['num_cores'] = new_df['num_cores'].str.replace('Quad Core','4')

new_df['num_cores'] = new_df['num_cores'].astype(float)

new_df.isnull().sum()

new_df.to_csv('smartphone_cleaned_final',index=False)