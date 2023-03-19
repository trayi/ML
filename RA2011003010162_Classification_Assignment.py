#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


# In[2]:


df=pd.read_excel('diabetes.xlsx')


# In[3]:


df.head()


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(df.drop('Outcome',axis=1), 
                                                    df['Outcome'], test_size=0.20, 
                                                    random_state=42)


# In[5]:


logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)


# In[6]:


predictions = logmodel.predict(X_test)


# In[7]:


score=accuracy_score(y_test,predictions)
score


# In[8]:


treemodel=DecisionTreeClassifier(random_state=0)


# In[9]:


treemodel.fit(X_train,y_train)


# In[10]:


predictions = treemodel.predict(X_test)


# In[11]:


score=accuracy_score(y_test,predictions)
score


# In[ ]:




