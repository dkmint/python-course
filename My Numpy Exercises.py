#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


arr = np.zeros(10)
arr


# In[4]:


ar = np.ones(10)
ar


# In[5]:


arr5 = np.zeros(10)
arr5[:]=5
arr5


# In[6]:


arr10 = np.arange(10, 51)
arr10


# In[7]:


arrEven = np.arange(10, 51, 2)
arrEven


# In[8]:


arr_1d = np.arange(0,9)
arr_2d = arr_1d.reshape(3,3)
arr_2d


# In[9]:


arreye = np.eye(3,3)
arreye


# In[10]:


np.random.rand()


# In[11]:


np.random.randn(26)


# In[32]:


arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1]
#Set up array

for i in range(arr_length):
#     arr2d[i] = i + 1/100
    for j in range(arr_length):
        arr2d[j] = j + 1/100
    
# arr2d


# In[77]:


arr2d = np.linspace(0,1,100).reshape(10,10)
arr2d[1:]


# In[70]:


np.linspace(0,1,20)


# In[78]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[79]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])


# In[89]:


mat[2:, 1:]


# In[90]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# 20


# In[103]:


mat[3,4]


# In[ ]:




