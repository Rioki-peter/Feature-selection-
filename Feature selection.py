#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
df=pd.read_csv("housing (1).csv")
df


# In[3]:


df.info()


# In[4]:


df.nunique() #checking canidalite for all columns


# In[5]:


df. ocean_proximity.value_counts()


# In[9]:


df2_price=pd.get_dummies(df,columns=["ocean_proximity"])
df2_price


# In[8]:


import matplotlib.pyplot as plt #visualization
import seaborn as sns # visualiazition 


# In[21]:


plt.figure(figsize=(15,12)) # correlation 
cor=df2_price.corr()
sns.heatmap(cor,annot=True,cmap="gist_rainbow_r")


# In[25]:


#specify the independent variable=median_house_value and arranging them in ascending order
cofficient =abs(cor["median_house_value"])
#cofficient=cofficient[cofficient>0.04]
cofficient.sort_values(ascending=False)


# In[21]:


#For specify columns only
df2_price=pd.get_dummies(df,columns=["ocean_proximity"])
df2_price.columns


# In[35]:


plt.figure(figsize=(15,12)) # correlation 
cor=df2_price[['total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']].corr()
sns.heatmap(cor,annot=True,cmap="cubehelix_r")


# In[ ]:




