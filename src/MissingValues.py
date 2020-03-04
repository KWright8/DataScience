#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
import pandas as pd

from pandas import Series,DataFrame


# ### Discovering Missing Values

# Missing values are called NaN values or Not a Number in python.
# Values you should also watch out for are 0s, 99s and 999s. They should be aproximated similarly to NaN values.
# 
# Missing values should be approximated not dropped.
# - First we shoud find all the missing values

# In[59]:


missing = np.nan

seriesObj = Series(['row 1','row 2','row 3',missing,'row 5','row 8',missing,'row 8','row 9','row 10',])
seriesObj


# Using .isnull() to locate all the places out series obj is null

# In[60]:


seriesObj.isnull()


# ### Aproximations for Missing Values

# To replace NaN Values we create a dataframe of random numbers

# In[61]:


np.random.seed(25)
dfObj = DataFrame(np.random.rand(36).reshape((6,6)))
dfObj


# In[62]:


dfObj.loc[3:5,0] = missing
dfObj.loc[1:4, 5] = missing
dfObj


# In[63]:


dfFilled = dfObj.fillna(0)
dfFilled


# Its nice to be able to fill all missing values with a number but what if we want some missing values 
# to equal one thing and others to equal something else? We can use the same .fillna() but instead of passing it an int we can pass it a dictionary where if the values at a location 5: for example it will recieve the value :12

# In[64]:


dfFilled = dfObj.fillna({0:1, 5:12})
dfFilled


# This is a little better but we want our predictions to be as accurate as possible so we should fill missing values with values that correspond with data in the dataframe. It is possible to pass a method to the .fillna() method. The ffill method will fill the missing value with the last non null value

# In[65]:


dfFilled = dfObj.fillna(method="ffill")
dfFilled


# ### Counting Missing Values

# Sometimes it is useful to know which values are missing from a dataset. It could give you insigt about the labels. Maybe labels with lots of missing values can be considered problemaatic.

# In[66]:


dfObj.loc[3:5,0] = missing
dfObj.loc[1:4, 5] = missing
dfObj


# isnull().sum() returns how many null values are in the column

# In[67]:


dfObj.isnull().sum()


# ### Filtering Out Missng Values

# To remove all rows with null values

# In[68]:


dfNoNa = dfObj.dropna()
dfNoNa


# Remove columns instead with missing values

# In[69]:


dfNoNa = dfObj.dropna(axis=1)
dfNoNa

