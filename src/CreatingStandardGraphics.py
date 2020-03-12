#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams


# Two methods for plot building:
# <br />
# <br />
# *Fuctional:* Call plotting method on a variable or a set of variable <br />
# *Obect-Oriented:* First gen. a blank figure object and populate it wih plots and plot elements.

# ### Practical Data Visualization 

# #### Segment 1 - Creating standard data graphcs

# ##### Plotting a line chart in matplotlib

# In[8]:


x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)


# #### Plotting a line chart from a Pandas object

# In[11]:


# Make sure to convert it to raw or it will create err
address = r"C:\Users\Keyana Wright\Desktop\DataScience\Ex_Files_Python_Data_Science_EssT_Pt_1\ExerciseFiles\Data\mtcars.csv"


cars = pd.read_csv(address)
cars.columns = ['Car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars['mpg']


# In[28]:


# plot the mpg
plt.plot(mpg)
plt.savefig("mpg.png")


# In[21]:


# create a plot of three different variables.
# create data frame
cylWtMpg = cars[['cyl','wt','mpg']]
hpMpg = cars[['hp', 'mpg']]

# plot
cylWtMpg.plot()
hpMpg.plot()


# ### Creating bar Bar Charts

# #### Creating bar charts from a list

# In[22]:


plt.bar(x,y)


# #### Creating bar charts from Pandas objects

# In[23]:


hpMpg.plot(kind="bar")


# In[24]:


cars.plot(kind="bar")


# ### Creating Pie Charts

# In[25]:


x = [1,2,3,4,0.5]

plt.pie(x)
plt.show()


# ### Saving Plots

# In[26]:


plt.pie(x)
plt.savefig("pie_chart.png")
plt.show()


# In[27]:





# In[ ]:




