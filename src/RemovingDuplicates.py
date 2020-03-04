#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as py
import pandas as pd
from pandas import Series,DataFrame


# Its important to remove duplicates from a data set so that the predictions are not skewed. For example if we are trying to make predictions about shoppers and one shopper in particular freq. the store we would only want to include that shoppers data once as one peron not three times as three different people.
# 
# - {} passing a dictionary

# In[10]:


dfObj = DataFrame({'Column 1':[1,1,2,2,3,3,3],
                   'Column 2':['a','a','b','b','c','c','c'],
                   'Column 3':['A','A','B','B','C','C','C']})
dfObj


# .duplicates() runs through the rows and checks if there has been a row seen that it is a duplicate of. If there is then the value stored for that row is true.

# In[11]:


dfObj.duplicated()


# To remove duplicates we use .drop_duplicates() 

# In[14]:


dfObj.drop_duplicates()


# Successfully removes all duplicates leavinng only rows 0,2 and 4

# You can also check for duplicates based on columns and remove based on columns

# In[16]:


dfObj = DataFrame({'Column 1':[1,1,2,2,3,3,3],
                   'Column 2':['a','a','b','b','c','c','c'],
                   'Column 3':['A','A','B','B','C','D','C']})
dfObj


# In[23]:


dfObj.drop_duplicates('Column 3')

