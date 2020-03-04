#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# ## Concatination and Data Transformation
# 
# - Important for getting data in the form you need to preform analysis
# 

# - .arange() when passed a value will generate values from 0 to that value noninclusive
# - .reshape() defines the shape of the dataframe

# In[7]:


dfObj = DataFrame(np.arange(36).reshape((6,6)))
dfObj


# We need to create another data frame to practice this

# In[11]:


dfObj2 = DataFrame(np.arange(15).reshape(5,3))
dfObj2


# ### Concatination
# - pd.concat(df1,df2, axis=1) setting the axis = 1 will indicate that you want to add the columns
# - pd.concat(df1,df2) without specfiying an axis will concat the rows 

# In[13]:


pd.concat([dfObj, dfObj2], axis=1)


# In[15]:


pd.concat([dfObj, dfObj2])


# ## Transforming Data

# ### Dropping data

# In[16]:


dfObj.drop([0,5])


# In[17]:


dfObj.drop([0,4], axis=1)


# ### Adding data

# In[22]:


seriesObj = Series(np.arange(6))
seriesObj.name = "AddedVar"
seriesObj


# In[24]:


varAdded = DataFrame.join(dfObj,seriesObj)
varAdded


# Instead of using the .join() method we can also use the appand() method. We can also preserve the indexing of both tables by passing ignore_index=False. Setting that value = to True will reindex the table

# In[31]:


doubleUpUsingAppend = varAdded.append(varAdded, ignore_index=False)
doubleUpUsingAppend


# In[30]:


doubleUpUsingAppend = varAdded.append(varAdded, ignore_index=True)
doubleUpUsingAppend


# ### Sorting data

# In[42]:


dfSorted = dfObj.sort_values(by=(5),ascending=False)
dfSorted

