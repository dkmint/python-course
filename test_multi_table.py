#!/usr/bin/env python
# coding: utf-8

# In[8]:


def scores(i):
    switcher={
        10:'5',
         9:'4',
         8:'4',
         7:'3',
    }
    return switcher.get(i,"2")


import numpy as np
print("***Test of knowledge of Multiplication Table***")
print("After example enter your answer and press <Enter>")
numOfCorrectAnss = 0

for i in range(0, 10):
    num1 = np.random.randint(1, 10)
    num2 = np.random.randint(1, 10)
    res = num1 * num2
    print(f"{num1} x {num2} = ")
    ans = int(input())
    if ans == res:
        numOfCorrectAnss += 1
    else:
        print(f"Wrong! {num1} x {num2} = {res} Let's continue...")

print(f"Correct answers: {numOfCorrectAnss}")
print("Your score: ")
scores(numOfCorrectAnss)


# In[ ]:




