#!/usr/bin/env python
# coding: utf-8

# In[3]:


def iterative_fib(n):
    count = 0
    n1 = 1
    n2 = 1
    fib_list =[]
    if n < 0:
        return "Please enter a positive number"
    elif(n == 0 or n ==1):
        return 1
    else:
        while count <= n:
            fib_list.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return fib_list[count-1]
    
def recurrent_fib(n):
    if n < 0:
        return "Please enter a positive number"
    if(n == 0 or n == 1):
        return 1
    if n > 0:
        return recurrent_fib(n - 1) + recurrent_fib(n -2)
    else:
        return "Oops something went wrong, please try again"


# In[5]:


iterative_fib(10)


# In[8]:


recurrent_fib(10)


# In[9]:


from timeit import default_timer as timer


def calculate_time_recurrent_fib(n):
    start = timer()
    recurrent_fib(n)
    end = timer()
    return end - start

def calculate_time_iterative_fib(n):
    start = timer()
    iterative_fib(n)
    end = timer()
    return end - start

time_iterative_fib_add =[]
for x in range(1,10000):
    time_iterative_fib_add.append(calculate_time_iterative_fib(x))
    


# In[14]:


import matplotlib.pyplot as plt
import numpy as np


font = {'family': 'serif',
        'color':  'DeepSkyBlue',
        'weight': 'normal',
        'size': 14,
        }


xpoints = list(range(1,10000))
ypoints = time_iterative_fib_add

plt.title('Fibonacci', fontdict=font, size = 20)
plt.xlabel('number of operations', fontdict=font)
plt.ylabel('time (s)', fontdict=font)

plt.plot(xpoints, ypoints, color = 'LightSkyBlue', linewidth = 2)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()


# In[16]:


time_iterative_fib =[]
time_recurrent_fib = []

for x in range(1,35):
    time_iterative_fib.append(calculate_time_iterative_fib(x))
    time_recurrent_fib.append(calculate_time_recurrent_fib(x)) 


# In[17]:


import matplotlib.pyplot as plt
import numpy as np


font = {'family': 'serif',
        'color':  'DeepSkyBlue',
        'weight': 'normal',
        'size': 14,
        }

    
xpoints = list(range(1,35))
ypoints = time_iterative_fib
ypoints1 = time_recurrent_fib

plt.title('Fibonacci', fontdict=font, size = 20)
plt.xlabel('number of operations', fontdict=font)
plt.ylabel('time (s)', fontdict=font)
plt.plot(xpoints, ypoints, color = 'cyan', linewidth = 2, label='Iterative Fibonacci')
plt.plot(xpoints, ypoints1, linestyle = 'dashed', linewidth = 2, label='Recurrent Fibonacci')
plt.legend()

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()


# In[ ]:




