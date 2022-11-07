#!/usr/bin/env python
# coding: utf-8

# In[145]:


import random

dataset = [random.randint(1,10000) for x in range(1,10000)]
dataset = sorted(dataset)

def recurrent_search(x, dataset):

    for idx, number in enumerate(dataset):
        if(x == number):
            return "The number you are looking for is in place number: " + str(idx)
    return -1

def iterative_search(search_number, dataset):
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


# In[148]:


recurrent_search(10000,dataset)


# In[151]:


iterative_search(10000,dataset)


# In[152]:


from timeit import default_timer as timer


def calculate_recurrent_search(n,dataset):
    start = timer()
    recurrent_search(n,dataset)
    end = timer()
    return end - start

def calculate_iterative_search(n,dataset):
    start = timer()
    iterative_search(n,dataset)
    end = timer()
    return end - start


# In[153]:


calculate_iterative_search(9997,dataset)


# In[154]:


calculate_recurrent_search(9997,dataset)

