#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

dataset = [random.randint(1,10000) for x in range(1,10000)]
dataset = sorted(dataset)

def linear_search(x, dataset):

    for idx, number in enumerate(dataset):
        if(x == number):
            return "The number you are looking for is in place number: " + str(idx)
    return -1

def exponential_search(search_number, dataset):
    left = 0 
    right = len(dataset) 
    index = 0 
    
    while left < right: 
        index = (left + right) // 2
        if dataset[index]==search_number: 
            return "The number you are looking for is in place number: " + str(index) 
        else: 
            if dataset[index]<search_number: 
                left = index+1 
            else: 
                right = index 

    return -1


# In[2]:


linear_search(10000,dataset)


# In[3]:


exponential_search(10000,dataset)


# In[4]:


from timeit import default_timer as timer


def calculate_linear_search(n,dataset):
    start = timer()
    linear_search(n,dataset)
    end = timer()
    return end - start

def calculate_exponential_search(n,dataset):
    start = timer()
    exponential_search(n,dataset)
    end = timer()
    return end - start


# In[5]:


calculate_exponential_search(9997,dataset)


# In[6]:


calculate_linear_search(9997,dataset)


# In[ ]:




