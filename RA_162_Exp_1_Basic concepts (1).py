#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import iqr 


# In[3]:


df=pd.read_csv("C:/Users/trid8/Downloads/gap.csv")


# In[4]:


df.groupby('continent')['lifeExp','gdpPercap'].mean()


# In[5]:


df.groupby('continent')['lifeExp','gdpPercap'].median()


# In[12]:


df.groupby('continent')['year','pop','lifeExp','gdpPercap'].agg(iqr)


# In[ ]:





# In[ ]:





# In[ ]:




