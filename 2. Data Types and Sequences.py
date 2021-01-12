#!/usr/bin/env python
# coding: utf-8

# # Data Types and Sequences 

# In[10]:


type('This is a string')


# In[11]:


type(None)


# In[12]:


type(1)


# In[13]:


type(1.0)


# In[14]:


type(add_numbers)
# add_numbers is defined as function in above code before


# In[15]:


# x written in parenthesis is tuple data type
x = (1, 'a', 2 , 'c')
type(x)


# In[18]:


# x written in square bracket is list data type
x = [1, 'a', 2 , 'c']
type(x)


# In[19]:


# append function
x.append(3.4)
print(x)


# In[20]:


for item in x:
    print(item)


# In[21]:


# Mathematical Operators - Plus, Multiple
[1, 2] + [3, 4]


# In[22]:


1 * 3


# In[23]:


# in function
1 in (1, 2, 3)


# # Strings 

# In[8]:


# String and numeric do not concatenate
# Eg: print('chris' + 2)


# In[3]:


print('Chris' + str(2))


# In[4]:


sales_record = {'price': 3.2,
               'num_items': 4, 
               'person': 'chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                            sales_record['num_items'],
                            sales_record['price'],
                            sales_record['num_items'] * sales_record['price']
                            ))


# In[ ]:




