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


# In[10]:


def findDog(dog):
#     if dog.lower() == True:
    sdog = dog.split()
    for s in sdog:
        if s == 'dog':
            print(True)
#     else:
#         print('The letters must be lower case.')
        
dog = 'Is there a dog here?'
findDog(dog)


# In[11]:


def countDog(str):
    count = 0
    lst = str.split()
    for l in lst:
        if l == 'dog':
            count += 1
    print(count)

str = 'This dog runs faster than the other dog dude!'
countDog(str)


# In[12]:


seq = ['soup','dog','salad','cat','great']
list(filter(lambda str: str[0] == 's', seq))


# In[26]:


def caught_speeding(speed, is_birthday):
    if speed <= 60:
        return 'No Ticket'
    elif is_birthday == True:
        return 'Small Ticket'
    elif speed > 61 and speed <= 80:
        return 'Small Ticket'
    else:
        return 'Big Ticket'


# In[28]:


caught_speeding(89,False)


# In[ ]:




