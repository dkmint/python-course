#!/usr/bin/env python
# coding: utf-8

# In[4]:


7**4


# In[5]:


s = 'Hi there Sam!'
s.split()


# In[6]:


planet = 'Earth'
diameter = 12742
'The diameter of {} is {} kilometers.'.format(planet, diameter)


# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]


# In[8]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# In[9]:


def domainGet(name):
    return name.split('@')[1]
    
domain = 'user@domain.com'    
domainGet(domain)


# In[4]:


def findDog(st):
    return 'dog' in st.lower().split()


# In[5]:


findDog('Is there a dog here?')


# In[6]:


# def countDog(str):
#     count = 0
#     lst = str.split()
#     for l in lst:
#         if l == 'dog':
#             count += 1
#     print(count)

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count

st = 'This dog runs faster than the other dog dude!'
countDog(st)


# In[12]:


seq = ['soup','dog','salad','cat','great']
list(filter(lambda str: str[0] == 's', seq))


# In[7]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[8]:


caught_speeding(89,False)


# In[ ]:




