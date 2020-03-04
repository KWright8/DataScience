#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# #### Grouping by column index

# ## Grouping and Aggregation
# - Reducing data down to inherent subgroups
# - useful when you want to compare subgroups
# - useful in understanding why groups differ
# - useful when you want to preform analysis on a specfic subgroup

# In[37]:


# Save the file path to our data. Make sure to convert it to raw.
address = r"C:\Users\Keyana Wright\Desktop\DataScience\Ex_Files_Python_Data_Science_EssT_Pt_1\ExerciseFiles\Data\mtcars.csv"

cars = pd.read_csv(address)
# Changing the labels for the columns
cars.columns = ['Names','MPG','CYL','DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']
# Print the first 5 entries
cars.head()

# Grouping cars by number of cylinders(4,6 and 8 cylinders). The other values are merged together by taking the mean of 
# values for that group. ex. the avg MPG for a 4 cylinder car is 26.67
gearGroup = cars.groupby(cars['CYL'])
gearGroup.mean()

