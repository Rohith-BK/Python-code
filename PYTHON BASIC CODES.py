#!/usr/bin/env python
# coding: utf-8

# ## PYTHON BASIC CODES

# In[2]:


# Import Libraries
import pandas as pd
import numpy as np


# In[14]:


from sklearn import preprocessing
import matplotlib.pyplot as plt


# In[3]:


plt.rc("font", size =14)


# In[4]:


from sklearn.linear_model import LogisticRegression


# In[5]:


from sklearn.model_selection import train_test_split


# In[6]:


import seaborn as sns


# In[7]:


sns.set(style ="white")


# In[8]:


import seaborn as sns

sns.set(style = "white")
sns.set(style = "whitegrid", color_codes = True)


# In[9]:


# Print working directory
import os
print(os.getcwd())
print(os.listdir(os.getcwd()))


# In[6]:


# Read CSV File
data =pd.read_csv("D:/TRAININGS-LEARNINGS/Python/bank.csv")

# To print heading of the data
data.head()


# In[4]:


# Read CSV File
data2 =pd.read_csv("../Documents/creditcard-sample.csv")

# To print heading of the data
data2.head()


# In[7]:


# List unique values of a variable. 
data['education'].unique()


# In[8]:


# Replace a value of a variable with other; replace 'basic.9y' with 'Basic' 
data['education']= np.where(data['education']=='basic.9y', 'Basic', data['education'] )


# In[9]:


data['education'].unique()


# In[10]:


data['y'].value_counts()


# In[17]:


# Getting Counts of different items in a varible 'education'
data['education'].value_counts()


# In[20]:


import seaborn as sns
graph = sns.countplot(x='y', data = data, palette = 'hls')


# In[21]:


plt.show()


# In[24]:


plt.savefig('count_plot')


# In[15]:


# Count number of datapoint by variable (when y is 0)
count1 = len(data[data['y'] == 0]) 
count1


# In[12]:


count2 = len(data[data['y']==1])
count2


# In[16]:


# Print numeric and text data in a print command
Percent_count = count1/count2
Percent_count
print('Ratio of counts', Percent_count*100)


# In[39]:


# Mean of all variable by groupby variable 'y'
Mean_data = data.groupby('y').mean()
Mean_data


# In[44]:


mean_data2 = data.groupby('job').mean()
# print(mean_data2)


# In[51]:


# Plotting Bar Charts using Pandas in (x, y) format for counts
pd.crosstab(data.job, data.y).plot(kind='bar')
plt.title('Purchase Frequency for Job Title')
plt.xlabel("job")
plt.ylabel('Y')
plt.savefig('Purchase-free-plot')


# In[33]:


# Current working directory
import os
os.getcwd()

# List directory  
os.listdir()

# change directory to Downloads
os.chdir("../Downloads/")

os.chdir("D:/CAPGEMINI-PROJECT/ALSTOM/data/")
os.getcwd()


# In[34]:


cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']


# In[35]:


cat_vars


# In[39]:


for var in cat_vars:
    cat_list = 'var' + '_' + 'var'


# In[37]:


cat_list


# In[58]:


# Histogram
data.job.hist()
plt.title('Histogram of Age')
plt.xlabel('List of jobs')
plt.ylabel('Number of observation')
plt.savefig('Plot of Histogram Age')


# In[ ]:




