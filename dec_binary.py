#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Converting of Decimal number into Binary one.\n")
dec = int(input("Enter integer number from 0 to 255 and press <Enter> "))
print(f"Decimal number {dec} corrsponds to a binary ", dec)
upCharge = 128
for i in range (1, 9):
    if dec >= upCharge:
        print('1', end = ' ')
        dec -= upCharge
    else:
        print("0", end = ' ')
    
    upCharge /= 2


# In[ ]:




