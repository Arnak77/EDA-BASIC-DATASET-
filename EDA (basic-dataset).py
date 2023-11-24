#!/usr/bin/env python
# coding: utf-8

# In[285]:


import pandas as pd


# # RAW DATA

# In[286]:


emp=pd.read_excel(r"D:\NIT\24NOV\23rd - Eda practicle\EDA- Practicle\Rawdata.xlsx")


# In[287]:


emp


# In[288]:


emp.columns


# In[289]:


emp.shape


# In[290]:


emp.head()


# In[291]:


emp.tail()


# In[292]:


emp.info()


# In[293]:


emp


# In[294]:


emp.columns


# In[295]:


emp['Domain']


# In[296]:


emp['Salary']


# In[297]:


emp.isnull()


# In[298]:


emp.isnull().sum()


# In[299]:


emp['Name']


# In[300]:


emp['Name'] = emp['Name'].str.replace(r'\W','',regex=True)


# In[301]:


emp


# In[302]:


emp['Name']


# In[303]:


emp['Domain']=emp['Domain'].str.replace(r'\W','' ,regex=True)


# In[304]:


emp['Domain']


# In[305]:


emp['Age']=emp['Age'].str.replace(r'\W','',regex=True)


# In[306]:


emp['Age']


# In[307]:


emp['Age']=emp['Age'].str.extract("(\d+)")


# In[308]:


emp['Age']


# In[309]:


emp['Salary']=emp['Salary'].str.replace('\W',"",regex=True)


# In[310]:


emp["Salary"]


# In[311]:


emp


# In[312]:


emp['Exp']=emp['Exp'].str.extract('(\d+)')


# In[313]:


emp['Exp']


# In[314]:


emp


# In[315]:


Clean_emp2=emp.copy()


# In[316]:


Clean_emp2


# In[317]:


Clean_emp2['Salary']


# In[318]:


import numpy as np


# In[319]:


Clean_emp2.isnull().sum()


# In[320]:


Clean_emp2


# In[321]:


Clean_emp2['Age']=Clean_emp2['Age'].fillna(np.mean(pd.to_numeric(Clean_emp2['Age'])))


# In[322]:


Clean_emp2


# In[323]:


Clean_emp2['Exp']=Clean_emp2['Exp'].fillna(np.mean(pd.to_numeric(Clean_emp2['Exp'])))


# In[324]:


Clean_emp2['Exp']


# In[325]:


Clean_emp2


# In[326]:


Clean_emp2['Location']=Clean_emp2['Location'].fillna(Clean_emp2['Location'].mode()[0])


# In[327]:


Clean_emp2['Location']


# In[328]:


Clean_emp2


# In[329]:


Clean_emp2.info()


# In[330]:


Clean_emp2.describe()


# In[331]:


Clean_emp2.isnull().sum()


# In[332]:


Clean_emp2.dtypes


# In[333]:


Clean_emp2['Age']=Clean_emp2["Age"].astype(int)


# In[334]:


Clean_emp2.dtypes


# In[335]:


Clean_emp2['Salary']=Clean_emp2['Salary'].astype(int)


# In[336]:


Clean_emp2['Exp']=Clean_emp2['Exp'].astype(int)


# In[337]:


Clean_emp2


# In[338]:


Clean_emp2.dtypes


# In[339]:


Clean_emp2.describe()


# In[340]:


Clean_emp2.info()


# In[341]:


Clean_emp2['Name']=Clean_emp2['Name'].astype('category')


# In[342]:


Clean_emp2


# In[343]:


Clean_emp2.dtypes


# In[344]:


Clean_emp2['Location']=Clean_emp2['Location'].astype('category')


# In[345]:


Clean_emp2['Domain']=Clean_emp2['Domain'].astype('category')


# # CLEAN DATA

# In[346]:


Clean_emp2


# In[347]:


Clean_emp2.dtypes


# In[348]:


Clean_emp2.to_csv('Clean_emp2.csv')


# In[349]:


import os
os.getcwd()


# In[350]:


Clean_emp2


# In[351]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[352]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[353]:


import warnings
warnings.filterwarnings('ignore')


# In[354]:


Clean_emp2['Salary']


# In[357]:


vis1=sns.distplot(Clean_emp2['Salary'])


# In[358]:


vis2=sns.distplot(Clean_emp2['Age'])


# In[361]:


vis2


# In[367]:


vis3=sns.histplot(Clean_emp2['Salary'])


# In[373]:


vis3=plt.hist(Clean_emp2['Salary'])


# In[375]:


vis2


# In[378]:


vis4=sns.lmplot(
    data=Clean_emp2,
    x="Exp",
    y='Salary')


# In[382]:


vis4=sns.lmplot(data=Clean_emp2,x='Age',y="Salary",fit_reg=False)


# In[387]:


Clean_emp2[:]


# In[388]:


Clean_emp2[0:6:2]


# In[389]:


Clean_emp2[::-1]


# In[390]:


X_iv =Clean_emp2[['Name', 'Domain', 'Age', 'Location', 'Exp']]


# In[391]:


X_iv


# In[392]:


Clean_emp2


# In[393]:


imputation=pd.get_dummies(Clean_emp2)


# In[394]:


imputation


# In[395]:


Clean_emp2


# In[396]:


imputation


# In[ ]:




