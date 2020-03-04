#!/usr/bin/env python
# coding: utf-8

# ## Filtering and selecting data

# In[29]:


import numpy as np
import pandas as pd

from pandas import Series,DataFrame


# ### Selecting and Retreiving Data
# 
# you can write the index in two ways
# - Label
# - Interger 

# ##### Series: Array
# Label Indexing:
# 1. create a series using the numpy arange function. It will have 10 values zero indexed. We will create label indexs
# 2. print series
# 
# The values stored at each index are the values 0-9 row 1 containing 0.

# In[39]:


seriesObj = Series(np.arange(10), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8','row 9','row 10'])
seriesObj


# Printing one index.

# In[40]:


seriesObj['row 8']


# Integer indexing:
# 1. print the values at index 1 and 8

# In[41]:


seriesObj[[1,8]]


# ###### DataFrame: Matrix
# 
# Creating a Dataframe with 36 random numbers. To generate the same numbers seed the random number generator with 25.
# Pass the random number that is generated. Reshape into a 6X6 lable rows and cloumns

# In[42]:


np.random.seed(25)
dfObj = DataFrame(np.random.rand(36).reshape((6,6)), 
                    index=['row 1','row 2','row 3','row 4','row 5','row 6'],
                    columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
dfObj


# You can isolate specfic rows and columns usng the .loc

# In[43]:


dfObj.loc[['row 1','row 5'],['column 3', 'column 4']]


# ### Data Slicing
# You pass it a starting index value and an ending index value. It will return the firs last and every record inbetween

# In[44]:


seriesObj['row 3':'row 9']


# ### Comparing values in series or dataframes with scalar values
# 
# Use coditional oporators with scalar quantities output true or false table 

# In[45]:


dfObj > 0.5


# ### Filtering Values With Scalars
# 
# filter out values based on specfic criteria

# In[46]:


seriesObj[seriesObj > 4]


# In[47]:


dfObj[dfObj > 0.5]


# (Above) NaN values do not meet the desired criteria

# ### Setting Values With Scalars

# In[49]:


seriesObj['row 2','row 9'] = 10000
seriesObj


# Using pandas to filter and select vlaues is fundamental to data analsis
