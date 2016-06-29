
# coding: utf-8

# In[59]:

'''
THIS PROJECT IS PART OF THE INTERVIEWING PROCESS FOR OPEN DATA FELLOW (KENYA) IN 2016
THE DATA USED IN THE PROJECT COMES FROM THE life_expectancy_in_counties.csv DATASET FOR 2016
The file is life_expectancy.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
get_ipython().magic(u'pylab inline')


# In[28]:

#importing the data
path = '/home/kev/Desktop/'
data = pd.read_csv(path+'Life_expectancy_in_counties.csv')
data['gender'] = data['gender'].astype('category')
data['county'] = data['county'].astype('category')
data.shape


# In[52]:

data.head()


# In[27]:

#cleaning the data
clean_data = data[data.county != 'Kenya']
clean_data = data.replace("Murang<U+201F>a", "Murang'a")


# In[48]:

#Zooming into the gender categories
p = clean_data.groupby('gender').describe()
p


# In[45]:

plt.figure(figsize=(14,10))
sns.set(font_scale=3)
sns.boxplot("life_expectancy", "gender", data=clean_data,saturation=.6, fliersize=10.)


# In[51]:

#To allow us to conduct further statistical analysis on the data, we need to reshape the data
piv_data = clean_data.pivot(index='county', columns='gender', values='life_expectancy')
piv_data


# In[70]:

#Correlation table showing the interaction between the four features in the data
corr = piv_data.corr()
fig, ax = plt.subplots(figsize=(14, 9))
plt.rc('xtick', labelsize=14) 
plt.rc('ytick', labelsize=20)
ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)


# In[67]:

corr


# In[ ]:



