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

# Another way doing this
# np.ones(10) * 5


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

# Another way doing this
# np.arange(9).reshape(3,3)


# In[9]:


arreye = np.eye(3,3)
arreye


# In[10]:


np.random.rand()

# Another way doing this
# np.random.rand(1)


# In[11]:


np.random.randn(25)


# In[119]:


np.arange(1,101).reshape(10,10) / 100


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


# In[104]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

# array([[ 2],
#        [ 7],
#        [12]])


# In[107]:


mat[:3, 1:2]


# In[108]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

# array([21, 22, 23, 24, 25])


# In[111]:


mat[4:]

# Another way doing this
# mat[4:,]


# In[112]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])


# In[120]:


mat[3:]

# Another way doing this
# may[3:5,:]


# In[114]:


mat.sum()


# In[115]:


mat.std()


# In[116]:


np.sum(mat, axis = 0)

# Another way doing this
# mat.sum(axis = 0)


# In[ ]:




